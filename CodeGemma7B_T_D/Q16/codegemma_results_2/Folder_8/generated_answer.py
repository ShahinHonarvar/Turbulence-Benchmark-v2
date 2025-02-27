def sum_even_ints_inclusive(num_list):
    sum = 0
    for num in num_list[23:25]:
        if num % 2 == 0:
            sum += num
    if sum == 0:
        return 0
    return sum