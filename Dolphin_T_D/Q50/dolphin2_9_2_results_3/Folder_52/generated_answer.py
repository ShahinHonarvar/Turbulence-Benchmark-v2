def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_pairs += 1
    return anagram_pairs >= 58