def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        word = string_list[i].lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            compare_word = string_list[j].lower()
            if len(compare_word) < 3:
                continue
            if sorted_word == ''.join(sorted(compare_word)):
                anagram_count += 1
                processed.add(j)
                if anagram_count >= 20:
                    return True
        processed.add(i)
    return False