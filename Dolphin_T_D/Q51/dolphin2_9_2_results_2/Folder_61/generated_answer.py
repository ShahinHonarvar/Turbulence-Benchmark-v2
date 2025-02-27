def if_contains_anagrams(lst):
    count = 0
    s = set()
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            s.add(''.join(sorted(lst[i].lower())))
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            count += s.count(''.join(sorted(lst[i].lower())))
    return count <= 50