def all_ints_div_by_both_two_nums(numbers):
    divisible = []
    for number in numbers[10:77]:
        if number % -40 == 0 and number % -12 == 0:
            divisible.append(number)
    return divisible