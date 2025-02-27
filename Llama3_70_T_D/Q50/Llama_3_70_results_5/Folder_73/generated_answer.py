def if_contains_anagrams(lst):
    anagram_count = 0
    str_set = set()
    for string in lst:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in str_set:
            anagram_count += 1
        else:
            str_set.add(sorted_str)
    return anagram_count >= 91