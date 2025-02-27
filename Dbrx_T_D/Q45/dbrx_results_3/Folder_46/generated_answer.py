from collections import defaultdict

def palindromes_between_indices(s):
    letters = s[4:10].lower()
    chars = defaultdict(int)
    for c in letters:
        chars[c] += 1
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            if chars[letters[j]] >= len(letters) - j:
                palindromes.add(letters[i:j + 1])
                chars[letters[j]] -= 1
    return {p for p in palindromes if len(p) >= 6}