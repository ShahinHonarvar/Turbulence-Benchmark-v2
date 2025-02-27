def gcf_three_nums(numbers):
    num1 = numbers[1]
    num2 = numbers[6]
    num3 = numbers[8]
    great_common_factor = int(min(num1, num2, num3))
    while great_common_factor > 1:
        if num1 % great_common_factor == 0 and num2 % great_common_factor == 0 and (num3 % great_common_factor == 0):
            return great_common_factor
        great_common_factor -= 1
    return 1