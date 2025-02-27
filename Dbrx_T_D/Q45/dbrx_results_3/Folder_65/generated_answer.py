from collections import defaultdict
import re

def palindromes_between_indices(s):
    s = s.lower()
    letters = defaultdict(int, {s[i]: i for i in range(7)})
    palindromes = set()
    for length in range(5, 7 + 1):
        for start in range(7 - length + 1):
            substring = ''.join(sorted(s[start:start + length]))
            if substring.isalpha() and any((substring[i] != substring[-i - 1] for i in range(length // 2))):
                palindrome = re.sub('[^\\w\\s]|_', '', substring[::-1] + substring[1:])
                if all((letters[c] <= letters[d] for c, d in zip(palindrome, palindrome[::-1]))):
                    palindromes.add(palindrome)
    return palindromes