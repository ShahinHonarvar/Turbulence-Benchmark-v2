def if_contains_anagrams(words):
    count = 0
    anagram_checked = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1, word2 = (words[i], words[j])
            if len(word1) >= 3 and len(word2) >= 3:
                sorted_word1 = ''.join(sorted(word1.lower()))
                sorted_word2 = ''.join(sorted(word2.lower()))
                if sorted_word1 == sorted_word2:
                    pair = tuple(sorted((word1, word2)))
                    if pair not in anagram_checked:
                        anagram_checked.add(pair)
                        count += 1
                        if count > 17:
                            return False
    return True