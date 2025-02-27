from collections import defaultdict

def build_palindrome_map(s):
    n = len(s)
    palindrome_map = defaultdict(set)
    for i in range(n):
        for j in range(i, n):
            if i == j or (s[i] == s[j] and (j - i == 1 or (j - i > 1 and i + 1 < j and (s[i + 1:j] in palindrome_map)))):
                palindrome_map[j - i].add(s[i:j + 1])
    return palindrome_map

def palindrome_of_length_n(s, n):
    s = ''.join((e for e in s if e.isalpha())).lower()
    if n % 2 == 0:
        n //= 2
    else:
        n = (n - 1) // 2
    palindrome_map = build_palindrome_map(s)
    return set(palindrome_map[n]) if n in palindrome_map else set()