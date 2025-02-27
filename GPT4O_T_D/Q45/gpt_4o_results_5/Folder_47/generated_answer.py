from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub_s = s[3:8].lower()
    english_letters = [ch for ch in sub_s if ch.isalpha()]
    if len(english_letters) < 5:
        return set()
    perms = set(permutations(english_letters))
    palindromes = set()
    for p in perms:
        combined = ''.join(p)
        for size in range(5, len(combined) + 1):
            for i in range(len(combined) - size + 1):
                sub = combined[i:i + size]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes