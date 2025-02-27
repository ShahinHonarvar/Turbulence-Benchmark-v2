def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 16:
        num = numbers[16]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect