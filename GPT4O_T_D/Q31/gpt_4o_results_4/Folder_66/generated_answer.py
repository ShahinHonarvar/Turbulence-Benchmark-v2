def if_perfect_num(numbers):
    if len(numbers) <= 42:
        return False
    number = numbers[42]
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number