def if_contains_anagrams(list_of_strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3]
    anagrams_count = 0
    pairs = {}
    for sorted_s in sorted_strings:
        if sorted_s not in pairs:
            pairs[sorted_s] = 1
        else:
            pairs[sorted_s] += 1
    for key in pairs:
        if pairs[key] > 1:
            anagrams_count += pairs[key] * (pairs[key] - 1) // 2
    return anagrams_count >= 74