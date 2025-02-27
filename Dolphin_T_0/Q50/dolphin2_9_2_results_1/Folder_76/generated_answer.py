def if_contains_anagrams(lst):
    count = 0
    sorted_lst = [''.join(sorted(i.lower())) for i in lst if len(i) >= 3]
    for i in range(len(sorted_lst)):
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[i] == sorted_lst[j]:
                count += 1
        if count >= 143:
            return True
    return False