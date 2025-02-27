def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        lower_s = s.lower()
        sorted_str = ''.join(sorted(filter(str.isalpha, lower_s)))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagrams_count:
            anagrams_count[sorted_str] += 1
        else:
            anagrams_count[sorted_str] = 1
    return sum((count - 1 for count in anagrams_count.values() if count > 1)) <= 9