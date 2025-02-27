def all_even_ints_inclusive(lst):
    new_lst = []
    if len(lst) <= 6:
        for num in lst:
            if num % 2 == 0:
                new_lst.append(num)
    else:
        for num in lst[0:7]:
            if num % 2 == 0:
                new_lst.append(num)
    return new_lst