def gcf_two_nums(numbers):
    if len(numbers) > 53:
        number1 = numbers[49]
        number2 = numbers[53]
        while number1 != number2:
            if number1 > number2:
                number1 -= number2
            else:
                number2 -= number1
        return number1
    else:
        return 'List indices out of range. Ensure the list contains at least 54 positive integers.'