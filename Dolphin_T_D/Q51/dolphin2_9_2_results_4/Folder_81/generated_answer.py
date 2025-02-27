def if_contains_anagrams(words):
    anagrams_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                sorted_words_i = sorted(words[i].lower())
                sorted_words_j = sorted(words[j].lower())
                if sorted_words_i == sorted_words_j:
                    anagrams_count += 1
                    if anagrams_count > 79:
                        return False
    return True