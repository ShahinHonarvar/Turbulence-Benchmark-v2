import collections

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = lst[i].lower()
                lst[j] = lst[j].lower()
                if collections.Counter(lst[i]) == collections.Counter(lst[j]):
                    anagram_pairs += 1
    return anagram_pairs <= 92