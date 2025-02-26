def sum_ints_div_by_either_nums(numbers):
    total = 0
    for num in numbers[20:36]:
        if num % -36 == 0 or num % -89 == 0:
            total += num
    return total