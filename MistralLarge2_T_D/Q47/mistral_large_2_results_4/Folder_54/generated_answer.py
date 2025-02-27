def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    result = set()
    substring = s[27:78]
    for length in range(18, 20):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate.lower())
    return result