def if_contains_anagrams(word_list):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and len(s1) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_anagram(word_list[i], word_list[j]):
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True