from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            for j in range(len(lst)):
                if lst[j] != word and Counter(lst[j].lower()) == c:
                    anagram_pairs += 1
    return anagram_pairs <= 44