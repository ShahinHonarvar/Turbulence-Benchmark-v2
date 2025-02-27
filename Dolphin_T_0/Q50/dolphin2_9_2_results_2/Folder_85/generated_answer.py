def if_contains_anagrams(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        if len(lst[i]) >= 3:
            for j in range(i + 1, n):
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count += 1
    return count >= 73