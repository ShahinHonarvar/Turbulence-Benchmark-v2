def if_perfect_num(numbers):
    if len(numbers) < 9:
        return False
    num = numbers[8]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num