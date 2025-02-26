from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    word_pairs = combinations(string_list, 2)
    for word1, word2 in word_pairs:
        if len(word1) >= 3 and len(word2) >= 3:
            if sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower():
                anagram_count += 1
                if anagram_count >= 10:
                    return True
    return False