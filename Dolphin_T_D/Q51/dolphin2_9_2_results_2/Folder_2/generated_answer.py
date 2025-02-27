from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i].lower()
            word2 = words[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
                anagram_pairs += 1
                if anagram_pairs > 81:
                    return False
    return anagram_pairs <= 81