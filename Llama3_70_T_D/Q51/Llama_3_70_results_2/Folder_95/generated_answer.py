def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]) and len(lst[i]) >= 3:
                anagrams_count += 1
                if anagrams_count > 6:
                    return False
    return True