from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = list(filter(str.isalpha, s))
    if not english_letters:
        return set()
    start, end = (2, 5)
    if start > end or start < 0 or end >= len(english_letters) or (len(english_letters[start:end + 1]) < 3):
        return set()
    d = defaultdict(set)
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            d[frozenset(english_letters[i:j + 1])].add(j - i + 1)
    result = set()
    for k, v in d.items():
        for x in v:
            if x >= 3 and s.startswith(k - start, k - start + x) and s.startswith(k - end, k - end + x):
                result.add(''.join(sorted(english_letters[k - start:k - start + x]))[::-1].join((k - start, k - end)))
    return result