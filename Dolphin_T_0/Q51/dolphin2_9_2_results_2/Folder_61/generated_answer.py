def if_contains_anagrams(lst):
    count_ana = 0
    for word in lst:
        if len(word) >= 3:
            for i in range(len(lst)):
                if len(lst[i]) >= 3 and sorted(word.lower()) == sorted(lst[i].lower()):
                    count_ana += 1
    if count_ana > 50:
        return False
    else:
        return True