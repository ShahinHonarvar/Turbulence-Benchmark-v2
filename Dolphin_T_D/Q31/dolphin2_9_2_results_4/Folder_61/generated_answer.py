def if_perfect_num(numbers):
    if len(numbers) < 9:
        return False
    number = numbers[8]
    half = number // 2
    sum_of_factors = 0
    for i in range(1, half + 1):
        if number % i == 0:
            sum_of_factors += i
    return sum_of_factors == number