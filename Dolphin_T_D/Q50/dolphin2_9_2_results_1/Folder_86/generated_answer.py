def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = sorted(lst[i].lower())
            str2 = sorted(lst[j].lower())
            if len(lst[i]) >= 3 and len(str1) == len(str2) and (str1 == str2):
                anagrams += 1
    if anagrams >= 115:
        return True
    else:
        return False