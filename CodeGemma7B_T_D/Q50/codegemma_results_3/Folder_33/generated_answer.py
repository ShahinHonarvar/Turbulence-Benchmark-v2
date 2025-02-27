def if_contains_anagrams(str_list):
    str_list = list(map(lambda s: ''.join(sorted(s.lower())), str_list))
    pairs = sum([1 for i in range(len(str_list)) for j in range(i + 1, len(str_list)) if str_list[i] == str_list[j]], 0)
    return pairs >= 210