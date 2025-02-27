def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def sort_text(text):
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word_i = words_list[i]
            word_j = words_list[j]
            if len(word_i) < 3 or len(word_j) < 3:
                continue
            normalized_word_i = normalize_text(word_i)
            normalized_word_j = normalize_text(word_j)
            sorted_word_i = sort_text(normalized_word_i)
            sorted_word_j = sort_text(normalized_word_j)
            if sorted_word_i == sorted_word_j:
                anagram_count += 1
                anagram_pairs.add(frozenset([word_i, word_j]))
            if anagram_count > 58:
                return False
    return True