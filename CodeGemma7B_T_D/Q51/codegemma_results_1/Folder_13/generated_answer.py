def if_contains_anagrams(str_list):
    str_map = {}
    str_count = {}
    for str in str_list:
        str = str.lower()
        sorted_str = ''.join(sorted(str))
        if sorted_str not in str_map:
            str_map[sorted_str] = str
            str_count[sorted_str] = 0
        else:
            str_count[sorted_str] += 1
    anagram_pairs = 0
    for count in str_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 54