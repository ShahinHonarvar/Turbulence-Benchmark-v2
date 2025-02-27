def if_perfect_num(numbers):
    if len(numbers) <= 78:
        return False
    number = numbers[78]
    if number <= 1:
        return False
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number