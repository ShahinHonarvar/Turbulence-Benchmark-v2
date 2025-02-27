from string import ascii_lowercase

def palindromes_between_indices(txt):
    seen = {0, len(txt)}
    for i in range(len(txt)):
        if txt[i] in ascii_lowercase:
            seen.add(i)
    seen = sorted(seen)
    pairs = []
    for i in range(len(seen) - 1):
        pairs.append((seen[i], seen[i + 1]))
    pairs.sort()
    results = set()
    for start, end in pairs:
        for c1 in range(start, end + 1):
            for c2 in range(start, end + 1):
                for c3 in range(start, end + 1):
                    if c1 < c2 < c3:
                        temp = ''.join(sorted([txt[i] for i in range(start, end + 1)]))
                        results.add(temp)
    return results