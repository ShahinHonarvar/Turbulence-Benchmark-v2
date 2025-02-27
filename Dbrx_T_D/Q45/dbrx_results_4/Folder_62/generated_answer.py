from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for start in range(0, min(9, len(s))):
        for end in range(start, min(9, len(s))):
            if end - start < 6:
                continue
            counter = defaultdict(int)
            for i in range(start, end + 1):
                counter[s[i]] += 1
            if all((count % 2 == 0 for count in counter.values())) or len([count for count in counter.values() if count % 2 == 1]) <= 1:
                palindromes.add(''.join(sorted(counter.keys())))
    return palindromes