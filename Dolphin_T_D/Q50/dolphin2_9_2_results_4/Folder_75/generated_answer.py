def if_contains_anagrams(l):
    anagram_count = 0
    for i, word1 in enumerate(l):
        if len(word1) >= 3:
            for word2 in l[i + 1:]:
                if sorted(word1.lower()) == sorted(word2.lower()):
                    anagram_count += 1
    return anagram_count >= 70