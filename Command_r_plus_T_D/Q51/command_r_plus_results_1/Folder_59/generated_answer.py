def if_contains_anagrams(words_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if is_anagram(words_list[i], words_list[j]) and len(words_list[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs > 15:
                    return False
    return True