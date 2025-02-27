def if_perfect_num(numbers):
    if len(numbers) >= 3:
        num = numbers[2]
        if num > 0:
            divisors = [i for i in range(1, num) if num % i == 0]
            return sum(divisors) == num
    return False