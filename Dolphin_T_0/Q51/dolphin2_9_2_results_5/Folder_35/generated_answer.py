from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = sorted(word.lower())
            for other_word in lst:
                if word != other_word and len(other_word) >= 3:
                    other_sorted_word = sorted(other_word.lower())
                    if sorted_word == other_sorted_word:
                        count += 1
    return count <= 210