from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:9].lower()
    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    palindromes = set()
    for i in range(1, 6):
        for j in range(0, len(s) - i + 1):
            can_be_palindrome = True
            for k in range(j, j + i):
                if s[k] != s[j - 1 + i - k]:
                    can_be_palindrome = False
                    break
            if can_be_palindrome:
                palindrome = ''.join(sorted(s[j:j + i]))
                if chars[list(palindrome)[0]] >= (j + i - 1) // 2 + 1:
                    palindromes.add(palindrome)
    return palindromes