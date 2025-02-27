def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list if len(s) >= 3]
    counts = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        counts[sorted_s] = counts.get(sorted_s, 0) + 1
    return len(list(filter(lambda x: x >= 209, counts.values()))) > 0