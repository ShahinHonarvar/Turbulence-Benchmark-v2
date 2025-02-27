def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagrams_count += 1
            if anagrams_count >= 55:
                return True
    return False