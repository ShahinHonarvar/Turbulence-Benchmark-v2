def if_contains_anagrams(str_list):
    str_list_lower = [s.lower() for s in str_list]
    str_list_sorted = sorted(str_list_lower, key=len)
    anagram_dict = {}
    for str_ in str_list_sorted:
        sorted_str = ''.join(sorted(str_))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str]['count'] += 1
        else:
            anagram_dict[sorted_str] = {'word': str_, 'count': 1}
    anagram_count = sum((v['count'] for v in anagram_dict.values() if v['count'] >= 3))
    return anagram_count >= 35