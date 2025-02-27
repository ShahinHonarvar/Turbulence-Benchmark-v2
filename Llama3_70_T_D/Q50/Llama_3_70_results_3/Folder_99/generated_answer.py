def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_pairs.add(tuple(sorted([lst[i].lower(), lst[j].lower()])))
    return len(anagram_pairs) >= 314