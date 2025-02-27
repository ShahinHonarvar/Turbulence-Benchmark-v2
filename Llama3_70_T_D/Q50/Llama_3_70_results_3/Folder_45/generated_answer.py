def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i].lower()) >= 3 and len(lst[j].lower()) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagram_count += 1
    return anagram_count >= 277