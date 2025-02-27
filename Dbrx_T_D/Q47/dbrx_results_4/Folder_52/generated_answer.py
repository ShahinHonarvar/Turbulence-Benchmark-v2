from collections import defaultdict

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        i, j = (0, len(s) - 1)
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    result = set()
    for length in range(13, 43):
        for start in range(44, 100 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring.lower())
    return result