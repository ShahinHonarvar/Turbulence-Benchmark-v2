def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            a = ''.join(filter(str.isalpha, lst[i].lower()))
            b = ''.join(filter(str.isalpha, lst[j].lower()))
            if len(a) >= 3 and len(b) >= 3 and (sorted(a) == sorted(b)):
                count += 1
    return count <= 97