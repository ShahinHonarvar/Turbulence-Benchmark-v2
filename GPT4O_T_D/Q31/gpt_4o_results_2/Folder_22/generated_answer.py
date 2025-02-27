def if_perfect_num(numbers):
    if len(numbers) > 72:
        num = numbers[72]
        if num > 0:
            divisors = [i for i in range(1, num) if num % i == 0]
            return sum(divisors) == num
    return False