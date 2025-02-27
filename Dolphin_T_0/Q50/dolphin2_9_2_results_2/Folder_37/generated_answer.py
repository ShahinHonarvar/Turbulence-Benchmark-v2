def if_contains_anagrams(list_of_strings):
    count = 0
    for word1 in list_of_strings:
        for word2 in list_of_strings:
            if len(word1) >= 3 and len(word2) >= 3 and (word1 != word2) and (word1.lower() == word2.lower()[::-1]):
                count += 1
    return count >= 29