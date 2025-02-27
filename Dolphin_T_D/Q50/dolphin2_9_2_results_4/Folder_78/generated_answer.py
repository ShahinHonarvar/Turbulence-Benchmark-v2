from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for anagram in (word.lower() for word in lst if len(word) >= 3):
                if Counter(word.lower()) == Counter(anagram) and word.lower() != anagram:
                    count += 1
    return count // 2 >= 79