def if_contains_anagrams(word_list):
    anagram_count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if sorted(word_list[i].lower()) == sorted(word_list[j].lower()):
                    anagram_count += 1
    return anagram_count >= 74