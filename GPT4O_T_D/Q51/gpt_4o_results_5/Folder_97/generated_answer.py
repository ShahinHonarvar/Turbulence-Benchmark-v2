from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)

    def normalize(word):
        return ''.join(sorted(filter(str.isalpha, word.lower())))
    normalized_strings = [(normalize(s), s) for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_anagram(normalized_strings[i][0], normalized_strings[j][0]):
                anagram_pairs += 1
                if anagram_pairs > 18:
                    return False
    return True