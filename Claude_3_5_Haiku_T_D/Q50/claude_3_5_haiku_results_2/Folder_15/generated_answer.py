def if_contains_anagrams(lst):

    def is_anagram(word1, word2):
        return len(word1) == len(word2) and len(word1) >= 3 and (sorted(word1.lower()) == sorted(word2.lower()))
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
    return anagram_pairs >= 4