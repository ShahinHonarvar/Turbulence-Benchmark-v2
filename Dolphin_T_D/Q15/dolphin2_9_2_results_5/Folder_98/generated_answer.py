def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(lst[0], lst[6] + 1):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd if sum_odd != 0 else 0