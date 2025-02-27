from collections import Counter

def if_contains_anagrams(lst):
    anagrams = [s for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if Counter(anagrams[i].lower()) == Counter(anagrams[j].lower()):
                anagram_pairs += 1
    if anagram_pairs <= 67:
        return True
    else:
        return False