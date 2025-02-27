def if_contains_anagrams(lst):
    anagram_count = 0
    str_set = set()
    sorted_str_dict = {}
    for string in lst:
        lower_str = string.lower()
        if len(lower_str) < 3:
            continue
        sorted_str = ''.join(sorted(lower_str))
        if sorted_str in sorted_str_dict:
            sorted_str_dict[sorted_str].append(lower_str)
        else:
            sorted_str_dict[sorted_str] = [lower_str]
    for lst in sorted_str_dict.values():
        if len(lst) > 1:
            anagram_count += len(lst) * (len(lst) - 1) // 2
    return anagram_count >= 246