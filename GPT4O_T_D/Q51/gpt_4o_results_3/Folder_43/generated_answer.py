def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    words = [word.lower() for word in words]
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if is_anagram(words[i], words[j]):
                    anagram_pairs.add((i, j))
                    if len(anagram_pairs) > 3:
                        return False
    return True