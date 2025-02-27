def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst) - 1):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 57 if anagram_pairs > 56 else False