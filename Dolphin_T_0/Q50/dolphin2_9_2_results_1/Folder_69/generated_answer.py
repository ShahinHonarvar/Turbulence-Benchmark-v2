def if_contains_anagrams(lst):
    anagrams_found = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagrams_found += 1
                if anagrams_found >= 188:
                    return True
    return False