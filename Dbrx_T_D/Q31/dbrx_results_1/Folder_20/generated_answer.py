def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 53:
        num = numbers[53]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect