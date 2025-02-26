def if_contains_anagrams(words):
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                sorted_word1 = sorted(words[i].lower())
                sorted_word2 = sorted(words[j].lower())
                if sorted_word1 == sorted_word2:
                    anagram_count += 1
                    if anagram_count > 67:
                        return False
    return True