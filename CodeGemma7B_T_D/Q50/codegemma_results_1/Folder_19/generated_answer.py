def if_contains_anagrams(str_list):
    str_set = set()
    anagram_count = 0
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower()))
        if sorted_str not in str_set:
            str_set.add(sorted_str)
        else:
            anagram_count += 1
    if anagram_count >= 84:
        return True
    else:
        return False