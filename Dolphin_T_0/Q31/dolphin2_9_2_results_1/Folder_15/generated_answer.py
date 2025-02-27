def if_perfect_num(numbers):
    if len(numbers) < 11:
        raise IndexError('List is not long enough, make sure it has at least 11 elements.')
    number = numbers[10]
    sum_factors = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum_factors += i
    return sum_factors == number