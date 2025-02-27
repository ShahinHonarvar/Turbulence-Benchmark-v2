def if_contains_anagrams(lst):
    count = 0
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            lst[i] = lst[i].lower()
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3:
                    lst[j] = lst[j].lower()
                    if sorted(lst[i]) == sorted(lst[j]) and lst[i] != lst[j]:
                        count += 1
                        if count > 277:
                            return False
    return True