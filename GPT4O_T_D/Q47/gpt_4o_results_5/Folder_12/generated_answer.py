def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[62:89]
    result = set()
    for length in range(18, 22):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            cleaned_candidate = ''.join(filter(str.isalpha, candidate)).lower()
            if len(cleaned_candidate) == length and is_palindrome(cleaned_candidate):
                result.add(candidate)
    return result