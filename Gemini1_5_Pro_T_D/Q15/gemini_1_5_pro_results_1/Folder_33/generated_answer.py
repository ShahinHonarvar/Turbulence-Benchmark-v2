def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(max(667, len(lst))):
        if i >= 667 and i <= 774 and (lst[i] % 2 != 0):
            sum += lst[i]
    return sum