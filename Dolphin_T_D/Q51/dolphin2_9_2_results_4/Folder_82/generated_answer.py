def if_contains_anagrams(lst):
    words = [word.lower() for word in lst]

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    for word1 in words:
        if len(word1) >= 3:
            for word2 in words:
                if word1 != word2 and is_anagram(word1, word2):
                    anagram_count += 1
                    if anagram_count > 40:
                        return False
    return True