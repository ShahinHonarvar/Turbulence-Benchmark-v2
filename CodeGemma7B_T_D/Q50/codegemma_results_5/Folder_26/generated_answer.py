def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_set = set()
    anagram_count = 0
    for string in str_list:
        if string in str_set:
            anagram_count += 1
        elif len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            str_set.add(sorted_str)
    return anagram_count >= 49