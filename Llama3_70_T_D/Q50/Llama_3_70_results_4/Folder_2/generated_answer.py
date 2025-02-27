def if_contains_anagrams(strings):
    anagrams_count = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagrams_count:
                anagrams_count[sorted_s] += 1
            else:
                anagrams_count[sorted_s] = 1
    count = 0
    for k, v in anagrams_count.items():
        count += v * (v - 1) // 2
    return count >= 246