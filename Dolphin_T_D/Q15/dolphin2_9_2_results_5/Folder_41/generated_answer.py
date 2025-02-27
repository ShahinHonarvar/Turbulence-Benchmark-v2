def sum_odd_ints_inclusive(lst):
    sum = 0
    for num in lst[6:7] + lst[7:8]:
        if num % 2 != 0:
            sum += num
    return sum