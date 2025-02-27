def if_perfect_num(numbers):
    if len(numbers) > 67:
        num = numbers[67]
        if num > 1:
            divisors = [i for i in range(1, num) if num % i == 0]
            return sum(divisors) == num
    return False