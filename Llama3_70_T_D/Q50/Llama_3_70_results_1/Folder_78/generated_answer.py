def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                pair = tuple(sorted([str1, str2]))
                anagram_pairs.add(pair)
    return len(anagram_pairs) >= 79