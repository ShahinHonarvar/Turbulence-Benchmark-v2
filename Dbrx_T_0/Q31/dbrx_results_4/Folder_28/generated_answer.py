def if_perfect_num(numbers):
    if len(numbers) > 37 and numbers[37] > 0:
        num = numbers[37]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False