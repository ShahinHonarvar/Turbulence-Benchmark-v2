def if_perfect_num(numbers):
    if len(numbers) > 263:
        num = numbers[263]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False