def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict and len(s) >= 3 and s.lower().isalpha():
            anagram_dict[sorted_str].append(s)
        elif len(s) >= 3 and s.lower().isalpha():
            anagram_dict[sorted_str] = [s]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += 1
        if count > 6:
            return False
    return True