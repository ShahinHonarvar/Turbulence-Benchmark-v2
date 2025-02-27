def if_contains_anagrams(words_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                if is_anagram(words_list[i], words_list[j]):
                    anagram_count += 1
                    if anagram_count >= 17:
                        return True
    return False