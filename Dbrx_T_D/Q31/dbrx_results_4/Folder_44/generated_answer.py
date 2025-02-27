def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 828 and numbers[828] > 0:
        num = numbers[828]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect