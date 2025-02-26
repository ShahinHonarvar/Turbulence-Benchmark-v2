def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_valid_anagram_pairs(words):
        valid_words = [word for word in words if len(word) >= 3]
        anagram_pairs = 0
        for i in range(len(valid_words)):
            for j in range(i + 1, len(valid_words)):
                if is_anagram(valid_words[i], valid_words[j]):
                    anagram_pairs += 1
        return anagram_pairs
    return count_valid_anagram_pairs(string_list) <= 276