def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                anagrams += 1
    return anagrams >= 9