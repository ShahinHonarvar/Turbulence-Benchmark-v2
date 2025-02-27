def sum_even_ints_inclusive(nums_list):
    sum = 0
    for num in nums_list[29:30]:
        if num % 2 == 0:
            sum += num
    return sum