def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    substring = s[18:89]
    for length in range(12, 15):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and candidate.isalpha() and (candidate.lower() == candidate):
                result.add(candidate)
    return result