def if_contains_anagrams(strings):
    anagrams_count = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams_count:
            anagrams_count[sorted_s] += 1
        else:
            anagrams_count[sorted_s] = 1
    pairs = sum((count - 1 for count in anagrams_count.values() if count > 1))
    return pairs <= 68