def all_neg_ints_exclusive(lst):
    negative_numbers = []
    for num in lst[1:-1]:
        if num < 0:
            negative_numbers.append(num)
    return negative_numbers