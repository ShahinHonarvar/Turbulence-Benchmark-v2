from collections import deque

def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        letters = deque(word)
        while len(letters) > 1:
            if letters.popleft() != letters.pop():
                return False
        return True
    result = set()
    s = s[10:56].lower()
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result