def sum_ints_div_by_either_nums(numbers):
    divisors = [-46, -82]
    return sum((num for num in numbers[48:77] if any((num % div % 2 == 0 for div in divisors)) or all((num % div == 0 for div in divisors))))