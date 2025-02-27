def if_perfect_num(numbers):
    if len(numbers) > 60:
        num = numbers[60]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False