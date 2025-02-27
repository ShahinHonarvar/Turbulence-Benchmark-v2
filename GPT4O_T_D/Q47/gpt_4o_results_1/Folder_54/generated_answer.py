def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    substring = s[27:78]
    for length in range(18, 20):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            cleaned_candidate = ''.join(filter(str.isalpha, candidate)).lower()
            if len(cleaned_candidate) == length and is_palindrome(cleaned_candidate):
                valid_palindromes.add(candidate[start:start + length])
    return valid_palindromes