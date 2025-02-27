from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for other_word in words:
                if other_word != word and len(other_word) >= 3:
                    other_sorted_word = ''.join(sorted(other_word.lower()))
                    if sorted_word == other_sorted_word:
                        anagram_pairs += 1
    return anagram_pairs >= 69