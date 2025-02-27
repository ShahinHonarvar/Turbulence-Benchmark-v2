def if_contains_anagrams(strings):
    anagrams_count = {}
    total_pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams_count:
            total_pairs += anagrams_count[sorted_s]
            anagrams_count[sorted_s] += 1
        else:
            anagrams_count[sorted_s] = 1
    return total_pairs <= 49