def if_contains_anagrams(lst):
    sorted_str_dict = {}
    anagram_pairs = 0
    for str in lst:
        if len(str) < 3:
            continue
        key = ''.join(sorted(str.lower()))
        if key in sorted_str_dict:
            sorted_str_dict[key] += 1
            anagram_pairs += sorted_str_dict[key]
        else:
            sorted_str_dict[key] = 1
    return anagram_pairs >= 189