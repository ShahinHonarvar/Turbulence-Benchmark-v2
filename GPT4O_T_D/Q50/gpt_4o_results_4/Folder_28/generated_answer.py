def if_contains_anagrams(strings):
    count = 0
    normalized = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    pairs_checked = set()
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i] == normalized[j]:
                pair_indices = (min(i, j), max(i, j))
                if pair_indices not in pairs_checked:
                    count += 1
                    pairs_checked.add(pair_indices)
                    if count >= 81:
                        return True
    return False