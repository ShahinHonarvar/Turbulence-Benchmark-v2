from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for other_word in lst:
                if len(word) != len(other_word):
                    continue
                if Counter(word.lower()) == Counter(other_word.lower()):
                    if word != other_word:
                        count += 1
    return count // 2 >= 74