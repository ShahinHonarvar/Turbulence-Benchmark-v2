def if_contains_anagrams(str_list):
    str_dict = {}
    str_len = len(str_list)
    for string in str_list:
        key = ''.join(sorted([char for char in string if char.lower() in 'abcdefghijklmnopqrstuvwxyz']))
        str_dict.setdefault(key, []).append(string)
    anagram_pairs = 0
    for key, value in str_dict.items():
        anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 401