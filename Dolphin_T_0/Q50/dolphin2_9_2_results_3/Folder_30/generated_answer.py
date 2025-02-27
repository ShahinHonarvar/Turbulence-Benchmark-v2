def if_contains_anagrams(lst):
    sorted_lst = [''.join(sorted(i.lower())) for i in lst if len(i) >= 3]
    counter = 0
    for i in range(len(sorted_lst)):
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[i] == sorted_lst[j]:
                counter += 1
    return counter >= 78