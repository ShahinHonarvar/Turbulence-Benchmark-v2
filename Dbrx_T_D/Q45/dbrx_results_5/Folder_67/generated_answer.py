import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(2, 7):
        if i < len(s):
            letters[s[i].lower()] += 1
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(length, len(letters) + 1):
            current = {k: v for k, v in letters.items() if v >= len(letters) - i + 1 and v <= i}
            if len(current) == length:
                palindrome = ''.join((k * v for k, v in current.items()))
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes