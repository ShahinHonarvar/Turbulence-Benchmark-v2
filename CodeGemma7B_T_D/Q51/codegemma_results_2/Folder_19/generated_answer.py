def if_contains_anagrams(str_list):
    str_set = set()
    anagram_pairs = 0
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        str_set.add(sorted_str)
        if sorted_str in str_set:
            anagram_pairs += 1
    if anagram_pairs <= 69:
        return True
    else:
        return False