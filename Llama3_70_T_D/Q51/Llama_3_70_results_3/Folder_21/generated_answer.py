def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i].casefold().isalpha() and lst[j].casefold().isalpha() and (len(lst[i]) >= 3) and (len(lst[j]) >= 3):
                if sorted(lst[i].casefold()) == sorted(lst[j].casefold()):
                    anagrams_count += 1
            if anagrams_count > 26:
                return False
    return True