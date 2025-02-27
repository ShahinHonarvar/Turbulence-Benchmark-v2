from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)}.union({chr(i) for i in range(ord('A'), ord('Z') + 1)})
    letters = defaultdict(int)
    start, end = (2, 3)
    for i in range(start, end + 1):
        if i < len(s) and s[i] in eng_letters:
            letters[s[i]] += 1
    palindromes = set()
    for length in range(3, len(letters) // 2 + 2):
        for comb in itertools.combinations(letters.keys(), length):
            if all((letters[char] >= count for char, count in Counter(comb).items())):
                palindromes.add(''.join(sorted(comb)))
    return {p.lower() for p in palindromes}