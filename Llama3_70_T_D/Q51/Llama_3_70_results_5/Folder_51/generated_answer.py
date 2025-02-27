def if_contains_anagrams(lst):
    anagrams_dict = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams_dict:
            anagrams_dict[sorted_str].append(s)
        else:
            anagrams_dict[sorted_str] = [s]
    for k, v in anagrams_dict.items():
        count += len(v) * (len(v) - 1) // 2
    return count <= 116