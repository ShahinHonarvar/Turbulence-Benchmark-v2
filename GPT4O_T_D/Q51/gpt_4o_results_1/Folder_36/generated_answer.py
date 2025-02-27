def if_contains_anagrams(strings):
    lowered_sorted = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    seen_pairs = set()
    for i in range(len(lowered_sorted)):
        for j in range(i + 1, len(lowered_sorted)):
            if lowered_sorted[i] == lowered_sorted[j]:
                pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    anagram_count += 1
                    if anagram_count > 25:
                        return False
    return True