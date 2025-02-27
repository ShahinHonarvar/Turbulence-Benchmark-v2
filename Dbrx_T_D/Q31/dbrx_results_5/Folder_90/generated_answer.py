def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 263:
        num = numbers[263]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            perfect = True
    return perfect