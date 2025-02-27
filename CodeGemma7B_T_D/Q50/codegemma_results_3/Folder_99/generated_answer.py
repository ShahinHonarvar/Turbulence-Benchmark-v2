def if_contains_anagrams(str_list):
    str_map = {}
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        str_map.setdefault(sorted_word, []).append(word)
    count = 0
    for anagram_list in str_map.values():
        for i in range(len(anagram_list)):
            for j in range(i + 1, len(anagram_list)):
                count += 1
                if count >= 314:
                    return True
    return False