def if_contains_anagrams(word_list):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    anagram_pairs = 0
    for word1 in word_list:
        for word2 in word_list:
            if is_anagram(word1, word2) and word1 != word2 and (len(word1) >= 3) and (len(word2) >= 3):
                anagram_pairs += 1
                word_list.remove(word1)
                word_list.remove(word2)
                break
        if len(word_list) < 2:
            break
    return anagram_pairs >= 44