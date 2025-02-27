def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i].lower() in lst[j].lower()) and (lst[j].lower() in lst[i].lower()):
                anagrams += 1
    if anagrams >= 54:
        return True
    return False