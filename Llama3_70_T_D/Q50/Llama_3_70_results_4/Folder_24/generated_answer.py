def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagrams_count += 1
    return anagrams_count >= 65