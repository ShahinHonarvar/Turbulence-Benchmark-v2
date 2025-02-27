from collections import deque

def palindromes_between_indices(s):
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(1, 8):
        for j in range(i, 8):
            substring = s[i - 1:j].lower()
            if len(substring) < 3:
                continue
            chars = deque(eng_letters)
            for char in substring:
                chars = [c for c in chars if c != char]
            while chars:
                palindrome = ''.join(chars)
                if palindrome == palindrome[::-1] and set(palindrome) == set(substring):
                    palindromes.add(palindrome)
                chars.append(chars.popleft())
    return palindromes