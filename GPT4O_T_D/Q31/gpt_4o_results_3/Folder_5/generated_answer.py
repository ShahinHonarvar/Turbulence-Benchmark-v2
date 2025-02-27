def if_perfect_num(numbers):
    if len(numbers) <= 67:
        return False
    num = numbers[67]
    if num <= 0:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num