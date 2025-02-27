def sum_odd_ints_inclusive(lst):
    if len(lst) < 71:
        return 0
    sum_odd = 0
    for num in lst[70:201]:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd