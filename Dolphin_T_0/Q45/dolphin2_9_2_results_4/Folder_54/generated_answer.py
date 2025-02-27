def palindromes_between_indices(s):
    s = ''.join((ch.lower() for ch in s[4:10] if ch.isalpha()))
    if len(set(s)) < 4:
        return set()
    return set((''.join(sorted(s)) for i in range(len(s)) for j in sorted(s) if len(palindrome_checker(''.join(sorted(s)), i, j)) >= 4))

def palindrome_checker(s, i, j):
    return s[i:j] + (s[:i] + s[j:])[::-1]