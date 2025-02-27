def if_perfect_num(numbers):
    if len(numbers) < 28:
        return False
    num = numbers[27]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num and num != 0:
        return True
    return False