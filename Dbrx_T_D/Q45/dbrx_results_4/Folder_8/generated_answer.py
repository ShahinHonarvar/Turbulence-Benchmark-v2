from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    for i in range(1, 6):
        for j in range(i, 6):
            letters = defaultdict(int, {c.lower(): s.count(c, i, j + 1) for c in set(s[i:j + 1])}.items())
            palindrome = ''
            for k in range(5, 0, -1):
                for c, count in letters.items():
                    if count >= k:
                        palindrome += c * k
                        letters[c] -= k
                        break
            if len(palindrome) >= 5:
                result.add(palindrome)
    return result