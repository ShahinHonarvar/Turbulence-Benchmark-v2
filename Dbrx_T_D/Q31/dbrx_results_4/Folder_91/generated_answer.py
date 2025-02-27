def if_perfect_num(numbers):
    if len(numbers) > 6:
        num = numbers[6]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False