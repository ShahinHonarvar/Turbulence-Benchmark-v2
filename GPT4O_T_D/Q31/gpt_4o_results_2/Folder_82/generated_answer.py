def if_perfect_num(numbers):
    if len(numbers) <= 83:
        return False
    number = numbers[83]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number