def all_ints_div_by_num(numbers):
    divisible_numbers = []
    for number in numbers:
        if number % 1 == 0:
            divisible_numbers.append(number)
    return divisible_numbers