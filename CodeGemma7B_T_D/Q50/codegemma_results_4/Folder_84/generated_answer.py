def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = {}
    count = 0
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in str_dict:
            str_dict[sorted_s] = []
        str_dict[sorted_s].append(s)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            for i in range(len(anagram_list)):
                for j in range(i + 1, len(anagram_list)):
                    if sorted(anagram_list[i]) == sorted(anagram_list[j]):
                        count += 1
    return count >= 108