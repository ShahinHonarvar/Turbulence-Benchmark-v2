from collections import deque

def palindromes_of_specific_lengths(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    s = ''.join((char for char in s[26:91] if char.isalpha())).lower()
    found_palindromes = set()
    for length in range(27, 59):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes