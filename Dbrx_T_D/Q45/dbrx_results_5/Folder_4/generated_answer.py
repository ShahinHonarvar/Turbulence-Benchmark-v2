from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:10].lower()
    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if sum((chars[char] for char in s[i:j + 1])) == (j - i + 1) // 2:
                palindromes.add(s[i:j + 1][::(j - i + 1) // 2])
    return palindromes