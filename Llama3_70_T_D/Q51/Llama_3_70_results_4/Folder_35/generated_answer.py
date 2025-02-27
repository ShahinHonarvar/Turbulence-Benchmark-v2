def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        sorted_str = ''.join(sorted(s))
        if len(s) < 3:
            continue
        anagrams_count[sorted_str] = anagrams_count.get(sorted_str, 0) + 1
    count = 0
    for value in anagrams_count.values():
        count += value * (value - 1) // 2
    return count <= 210