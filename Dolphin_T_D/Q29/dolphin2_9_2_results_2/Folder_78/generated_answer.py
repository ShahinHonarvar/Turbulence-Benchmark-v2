def gcf_two_nums(numbers_list):
    number1 = numbers_list[54]
    number2 = numbers_list[13]
    i = min(number1, number2)
    while i > 1:
        if number1 % i == 0 and number2 % i == 0:
            return i
        i -= 1
    return 1