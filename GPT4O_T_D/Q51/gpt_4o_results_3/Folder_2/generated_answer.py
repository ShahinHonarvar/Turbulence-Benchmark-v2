def if_contains_anagrams(lst):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    checked_words = []
    for i in range(len(lst)):
        word_i = lst[i]
        if len(word_i) < 3:
            continue
        sorted_word_i = sorted_lower(word_i)
        for j in range(i + 1, len(lst)):
            word_j = lst[j]
            if len(word_j) < 3:
                continue
            sorted_word_j = sorted_lower(word_j)
            if sorted_word_i == sorted_word_j:
                if (word_i, word_j) not in checked_words:
                    anagram_pairs += 1
                    checked_words.append((word_j, word_i))
                    if anagram_pairs > 81:
                        return False
    return anagram_pairs <= 81