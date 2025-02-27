def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        if not word.isalpha() or len(word) < 3:
            continue
        temp_word = ''.join(sorted(word.lower()))
        if temp_word in str_dict:
            str_dict[temp_word] += 1
        else:
            str_dict[temp_word] = 1
    anagram_count = 0
    for value in str_dict.values():
        if value >= 2:
            anagram_count += value * (value - 1) // 2
    return anagram_count >= 140