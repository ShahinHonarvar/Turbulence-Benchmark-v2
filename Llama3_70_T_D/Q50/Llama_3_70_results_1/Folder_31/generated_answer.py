def if_contains_anagrams(strings):
    anagram_count = 0
    seen = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        if sorted_s in seen:
            seen[sorted_s].append(lower_s)
        else:
            seen[sorted_s] = [lower_s]
    for anagrams in seen.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 68