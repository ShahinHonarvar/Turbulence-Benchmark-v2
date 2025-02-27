def if_perfect_num(numbers):
    if len(numbers) <= 702:
        return False
    num = numbers[702]
    if num <= 1:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num