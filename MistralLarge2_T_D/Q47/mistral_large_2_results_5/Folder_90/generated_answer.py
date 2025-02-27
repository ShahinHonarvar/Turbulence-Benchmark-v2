from collections import deque

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        dq = deque(sub.lower())
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
    palindromes = set()
    substr = s[106:281]
    for length in range(136, 152):
        for start in range(281 - length + 1):
            sub = substr[start:start + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes