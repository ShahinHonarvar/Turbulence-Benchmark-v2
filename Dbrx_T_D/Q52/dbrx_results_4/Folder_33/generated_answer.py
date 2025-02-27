from collections import defaultdict

def palindrome_of_length_n(s):
    n = 475
    s = ''.join((e for e in s if e.isalpha())).lower()
    if len(s) < n:
        return set()
    palindromes = set()
    char_count = defaultdict(int)
    for i in range(len(s) - n + 1):
        current_s = s[i:i + n]
        if all((x not in current_s for x in ('a', 'e', 'i', 'o', 'u'))):
            continue
        for j in range(n):
            char_count[current_s[j]] += 1
        if len(char_count) == n // 2 + 1:
            palindromes.add(current_s)
        char_count = defaultdict(int)
    return palindromes