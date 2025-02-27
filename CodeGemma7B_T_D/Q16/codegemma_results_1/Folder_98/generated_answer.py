def sum_even_ints_inclusive(list_of_nums):
    sum = 0
    for idx in range(0, 7):
        if list_of_nums[idx] % 2 == 0:
            sum += list_of_nums[idx]
    if sum == 0:
        return 0
    else:
        return sum