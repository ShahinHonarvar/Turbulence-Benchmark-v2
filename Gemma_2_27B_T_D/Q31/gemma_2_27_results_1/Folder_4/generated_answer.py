def if_perfect_num(numbers):
    sum_of_divisors = 1
    for i in range(2, int(numbers[15] ** 0.5) + 1):
        if numbers[15] % i == 0:
            sum_of_divisors += i + numbers[15] // i
    return sum_of_divisors == numbers[15]