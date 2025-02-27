def palindromes_of_specific_lengths(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    normalized = ''.join((c for c in s if c.isalpha())).lower()
    result_set = set()
    for i in range(12, 86):
        for length in range(4, 6):
            if i + length <= 87:
                substring = normalized[i:i + length]
                if is_palindrome(substring):
                    result_set.add(substring)
    return result_set