def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) < 3:
            continue
        count += len(group) * (len(group) - 1) // 2
    return count >= 74