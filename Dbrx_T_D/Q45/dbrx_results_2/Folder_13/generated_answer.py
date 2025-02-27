from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(3, 10):
        letters[s[i].lower()] += 1
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i + 5, min(len(s), i + 10)):
            substr = s[i:j].lower()
            if substr == substr[::-1] and all((letters[char] >= substr.count(char) for char in set(substr))):
                palindromes.add(substr)
    return palindromes