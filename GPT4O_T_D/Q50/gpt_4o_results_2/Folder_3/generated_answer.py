def if_contains_anagrams(strings):
    count = 0
    normalized = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen_pairs = set()
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i] == normalized[j]:
                pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    count += 1
                    if count >= 30:
                        return True
    return False