from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst1 = sorted(lst[i].lower())
                lst2 = sorted(lst[j].lower())
                if Counter(lst1) == Counter(lst2):
                    anagram_count += 1
                    if anagram_count > 392:
                        return False
    return anagram_count <= 392