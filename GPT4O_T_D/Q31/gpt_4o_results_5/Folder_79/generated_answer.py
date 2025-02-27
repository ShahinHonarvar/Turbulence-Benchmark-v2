def if_perfect_num(numbers):
    if len(numbers) <= 63:
        return False
    number = numbers[63]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number