def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [sorted(s) for s in str_list]
    sorted_strings_dict = {}
    for i, s in enumerate(str_list):
        if ''.join(s) not in sorted_strings_dict:
            sorted_strings_dict[''.join(s)] = []
        sorted_strings_dict[''.join(s)].append(i)
    anagram_pairs = 0
    for key, indices in sorted_strings_dict.items():
        if len(indices) > 1:
            anagram_pairs += len(indices) - 1
    return anagram_pairs <= 61