def all_ints_div_by_both_two_nums(numbers):
    start_index = 828
    end_index = 932
    divisors = (-649, -461)
    return [num for num in numbers[start_index:end_index + 1] if all((num % divisor == 0 for divisor in divisors))]