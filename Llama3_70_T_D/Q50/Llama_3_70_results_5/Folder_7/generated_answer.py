def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagrams_count += 1
    return anagrams_count >= 178