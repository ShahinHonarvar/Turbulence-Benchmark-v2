from collections import defaultdict

def palindrome_of_length_n(s, target_length=407):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < target_length:
        return set()
    palindromes = set()
    letters = defaultdict(int)
    for i in range(len(s)):
        letters[s[i]] += 1
        if i > target_length - 1:
            letters[s[i - target_length]] -= 1
            if letters[s[i - target_length]] == 0:
                del letters[s[i - target_length]]
        if i >= target_length - 1:
            if all((letters[c] % 2 == 0 for c in letters.keys())) and all((c in letters.keys() for c in s[i - target_length + 1:i + 1] if s[i] != c)):
                palindromes.add(s[i - target_length + 1:i + 1])
    return palindromes