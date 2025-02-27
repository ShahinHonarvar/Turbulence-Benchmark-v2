def all_ints_div_by_num(numbers):
    divisible_numbers = []
    for num in numbers:
        if num % 2 == 0:
            divisible_numbers.append(num)
    return divisible_numbers