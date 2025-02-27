def if_contains_anagrams(words):
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i].lower()
            word2 = words[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                pair = tuple(sorted([word1, word2]))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    anagram_count += 1
                    if anagram_count >= 95:
                        return True
    return False