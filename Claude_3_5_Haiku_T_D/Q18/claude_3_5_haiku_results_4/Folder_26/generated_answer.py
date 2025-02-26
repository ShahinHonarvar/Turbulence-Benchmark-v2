def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[69:71]:
        if num % 72 == 0 or num % 70 == 0:
            total += num
    return total