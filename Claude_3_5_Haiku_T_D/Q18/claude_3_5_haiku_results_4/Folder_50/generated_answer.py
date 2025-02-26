def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[46:92]:
        if num % 67 == 0 or num % 15 == 0:
            total += num
    return total