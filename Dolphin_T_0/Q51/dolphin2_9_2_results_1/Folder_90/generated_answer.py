from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            for other_word in lst:
                if len(other_word) >= 3:
                    other_word = other_word.lower()
                    sorted_other = ''.join(sorted(other_word))
                    if word != other_word and sorted_word == sorted_other:
                        anagram_pairs += 1
    return anagram_pairs // 2 <= 147