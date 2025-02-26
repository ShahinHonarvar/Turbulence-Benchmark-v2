def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed or len(string_list[i]) < 3:
            continue
        word = string_list[i].lower()
        sorted_word = ''.join(sorted(word))
        for j in range(i + 1, len(string_list)):
            if j in processed or len(string_list[j]) < 3:
                continue
            compare_word = string_list[j].lower()
            if len(word) == len(compare_word) and sorted_word == ''.join(sorted(compare_word)):
                anagram_count += 1
                processed.add(j)
                if anagram_count >= 24:
                    return True
        processed.add(i)
    return False