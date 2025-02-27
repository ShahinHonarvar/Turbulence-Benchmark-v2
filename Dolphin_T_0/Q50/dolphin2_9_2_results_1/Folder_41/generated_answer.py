def if_contains_anagrams(words):
    anagrams = 0
    for word1 in words:
        if len(word1) >= 3:
            for word2 in words:
                if word1.lower() != word2.lower() and sorted(word1.lower()) == sorted(word2.lower()):
                    anagrams += 1
    return anagrams >= 75