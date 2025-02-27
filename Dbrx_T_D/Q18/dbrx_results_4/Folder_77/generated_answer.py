def sum_ints_div_by_either_nums(numbers):
    divisors = [-649, -461]
    start_index = 828
    end_index = 932
    sum = 0
    for i in range(start_index, end_index + 1):
        if any((num % divisor == 0 for num in [numbers[i]] for divisor in divisors)):
            sum += numbers[i]
    return sum