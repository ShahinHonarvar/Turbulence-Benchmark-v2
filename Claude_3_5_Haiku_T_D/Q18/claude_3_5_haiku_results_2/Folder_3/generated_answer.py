def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(38, 53):
        if i < len(numbers):
            num = numbers[i]
            if num % -41 == 0 or num % -47 == 0:
                total += num
    return total