from collections import defaultdict

def palindromes_between_indices(s):
    s = s[4:6].lower()
    letters = defaultdict(int)
    for char in s:
        letters[char] += 1
    palindromes = set()
    for i in range(3, 101):
        if sum((s > chars for chars in letters.values())) < 3:
            break
        perms = [''.join(p) for p in permutations(s, i)]
        case_insensitive_perms = {''.join(p).lower() for p in permutations(s.upper(), i)}
        case_insensitive_perms.update({''.join(p).lower() for p in permutations(s.lower(), i)})
        palindromes.update(perms & case_insensitive_perms)
    return palindromes