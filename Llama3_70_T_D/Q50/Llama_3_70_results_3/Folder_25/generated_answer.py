def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_count += 1
    return anagram_count >= 14