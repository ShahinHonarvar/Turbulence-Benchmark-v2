def sum_even_ints_inclusive(num_list):
    sum_even = 0
    for num in num_list:
        if num % 2 == 0 and num_list.index(num) in range(6, 6 + 1):
            sum_even += num
    if sum_even == 0:
        return 0
    else:
        return sum_even