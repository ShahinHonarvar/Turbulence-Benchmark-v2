def if_contains_anagrams(lis):
    mod_lis = [i.lower() for i in lis if len(i) >= 3]
    count = 0
    for i in mod_lis:
        for j in mod_lis:
            if i != j and sorted(i) == sorted(j):
                count += 1
    return count >= 96