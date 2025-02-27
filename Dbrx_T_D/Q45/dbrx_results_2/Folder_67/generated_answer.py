from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    char_count = defaultdict(int)
    for i in range(2, 7):
        if 0 <= i < len(s):
            char_count[s[i]] += 1
    palindromes = set()
    for _ in range(5, 0, -1):
        for perm in itertools.permutations(char_count.keys(), _):
            if perm == perm[::-1]:
                if len(perm) >= 5:
                    palindromes.add(''.join(perm))
    return palindromes