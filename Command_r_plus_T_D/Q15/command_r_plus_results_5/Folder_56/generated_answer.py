def sum_odd_ints_inclusive(numbers_list):
    sum_odd = 0
    for num in numbers_list:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd