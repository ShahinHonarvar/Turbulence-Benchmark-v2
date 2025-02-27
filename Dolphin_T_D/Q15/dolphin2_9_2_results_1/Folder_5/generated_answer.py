def sum_odd_ints_inclusive(lst):
    sum_ = 0
    for num in lst[8:10]:
        if num % 2 == 1:
            sum_ += num
    return sum_ if sum_ else 0