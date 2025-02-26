def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                word1 = sorted(words[i].lower())
                word2 = sorted(words[j].lower())
                if word1 == word2:
                    anagram_pairs += 1
                    if anagram_pairs > 257:
                        return False
    return True