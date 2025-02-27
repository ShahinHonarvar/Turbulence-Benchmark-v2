def if_contains_anagrams(strings):
    anagrams_count = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams_count[sorted_s] = anagrams_count.get(sorted_s, 0) + 1
    pairs = 0
    for count in anagrams_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 61