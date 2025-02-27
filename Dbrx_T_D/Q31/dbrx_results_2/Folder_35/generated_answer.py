def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 993:
        num = numbers[993]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect