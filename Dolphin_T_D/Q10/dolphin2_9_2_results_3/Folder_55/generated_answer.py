def all_odd_ints_exclusive(lst):
    odd_lst = []
    for num in lst[2:-2]:
        if num % 2 != 0:
            odd_lst.append(num)
    return odd_lst