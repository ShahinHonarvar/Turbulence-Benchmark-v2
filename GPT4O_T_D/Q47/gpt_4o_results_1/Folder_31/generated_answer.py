def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    filtered_s = ''.join((c.lower() for c in s if c.isalpha()))
    for start in range(11, 84):
        for length in range(37, 61):
            if start + length <= len(filtered_s) + 11:
                substring = filtered_s[start - 11:start - 11 + length]
                if is_palindrome(substring):
                    result.add(substring)
    return result