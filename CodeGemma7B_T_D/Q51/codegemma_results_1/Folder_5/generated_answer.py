def if_contains_anagrams(string_list):
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) != len(string_list[j]):
                continue
            char_list1 = list(string_list[i].lower())
            char_list2 = list(string_list[j].lower())
            char_list1.sort()
            char_list2.sort()
            if char_list1 == char_list2:
                anagram_count += 1
    if anagram_count <= 4:
        return True
    else:
        return False