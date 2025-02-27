def if_perfect_num(numbers):
    if len(numbers) <= 73:
        return False
    number = numbers[73]
    if number <= 1:
        return False
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number