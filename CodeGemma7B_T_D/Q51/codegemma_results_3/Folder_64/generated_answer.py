def if_contains_anagrams(str_list):
    lower_str_list = [s.lower() for s in str_list]
    filtered_str_list = [s for s in lower_str_list if len(s) >= 3]
    anagram_dict = {}
    for s in filtered_str_list:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    count_pairs = 0
    for group in anagram_dict.values():
        count_pairs += int(len(group) * (len(group) - 1) / 2)
    return count_pairs <= 59