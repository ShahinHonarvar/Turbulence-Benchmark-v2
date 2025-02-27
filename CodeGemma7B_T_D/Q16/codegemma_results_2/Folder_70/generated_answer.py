def sum_even_ints_inclusive(int_list):
    sum = 0
    for num in int_list[28:33]:
        if num % 2 == 0:
            sum += num
    return sum if sum else 0