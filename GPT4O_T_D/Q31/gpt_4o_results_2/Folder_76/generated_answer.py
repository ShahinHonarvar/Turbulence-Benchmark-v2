def if_perfect_num(numbers):
    if len(numbers) <= 537:
        return False
    num = numbers[537]
    if num < 2:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num