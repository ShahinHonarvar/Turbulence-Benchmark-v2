def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    valid_range = s[21:63]
    result = set()
    for start in range(len(valid_range)):
        for length in range(22, 34):
            end = start + length
            if end <= len(valid_range):
                substring = valid_range[start:end]
                if substring.isalpha() and is_palindrome(substring.lower()):
                    result.add(substring)
    return result