def if_contains_anagrams(strings):
    anagrams_count = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams_count:
            anagrams_count[sorted_str] += 1
        else:
            anagrams_count[sorted_str] = 1
    pairs = 0
    for count in anagrams_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 75