def gcf_two_nums(numbers):
    num1 = numbers[78]
    num2 = numbers[16]
    factor = min(num1, num2)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1