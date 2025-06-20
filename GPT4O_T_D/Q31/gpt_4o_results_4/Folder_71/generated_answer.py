def if_perfect_num(numbers):
    if len(numbers) <= 78:
        return False
    num = numbers[78]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num