from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (words[i], words[j]) not in checked_pairs and len(words[i]) >= 3 and (len(words[j]) >= 3):
                if is_anagram(words[i], words[j]):
                    anagram_pairs += 1
                    checked_pairs.add((words[i], words[j]))
                    checked_pairs.add((words[j], words[i]))
                if anagram_pairs > 210:
                    return False
    return True