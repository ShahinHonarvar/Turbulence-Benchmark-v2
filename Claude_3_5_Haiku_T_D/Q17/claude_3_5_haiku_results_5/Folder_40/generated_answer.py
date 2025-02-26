def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 2:
        return []
    divisors = numbers[0:2]
    return [num for num in numbers if all((num % divisor == 0 for divisor in divisors))]