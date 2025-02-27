from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)}.union({chr(i) for i in range(ord('A'), ord('Z') + 1)})
    palindromes = set()
    for i in range(4, 10):
        for j in range(len(s) - i + 1):
            if s[j:j + i] in palindromes:
                continue
            if all((c not in english_letters for c in s[j:j + i])):
                continue
            if len(set(s[j:j + i]) & english_letters) < 2:
                continue
            s_map = defaultdict(int)
            for c in s[j:j + i]:
                s_map[c] += 1
            if all((count % 2 == 0 for count in s_map.values())) or sum((count % 2 for count in s_map.values())) == 1:
                palindromes.add(''.join((c for c in s[j:j + i] if c in english_letters)))
    return palindromes