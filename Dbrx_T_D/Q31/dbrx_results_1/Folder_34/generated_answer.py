def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 97:
        num = numbers[97]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect