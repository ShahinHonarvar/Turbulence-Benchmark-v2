def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def sorted_chars(text):
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word_i = normalize_text(words_list[i])
            word_j = normalize_text(words_list[j])
            if len(word_i) >= 3 and len(word_j) >= 3:
                if sorted_chars(word_i) == sorted_chars(word_j):
                    if (word_i, word_j) not in anagram_pairs and (word_j, word_i) not in anagram_pairs:
                        anagram_pairs.add((word_i, word_j))
                        anagram_count += 1
                    if anagram_count > 279:
                        return False
    return True