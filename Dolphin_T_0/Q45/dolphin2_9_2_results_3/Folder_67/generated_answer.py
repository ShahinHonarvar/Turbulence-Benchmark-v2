import itertools

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s)
    if len(letters) < 5:
        return set()
    palindromes = set()
    for p in range(5, len(s) + 1):
        for t in itertools.permutations(letters, p):
            words = set()
            for i in range(p):
                for j in range(i + 1, p):
                    if s[i] == t[j]:
                        words.add(s[i:j + 1])
            for word in words:
                if word == word[::-1] and len(word) >= 5:
                    palindromes.add(word)
    return palindromes