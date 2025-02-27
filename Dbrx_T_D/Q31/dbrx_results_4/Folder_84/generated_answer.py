def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 685 and numbers[685] > 0:
        num = numbers[685]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            perfect = True
    return perfect