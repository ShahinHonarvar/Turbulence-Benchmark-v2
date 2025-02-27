def if_perfect_num(numbers):
    if len(numbers) <= 74:
        return False
    n = numbers[74]
    return n == sum((i for i in range(1, n) if n % i == 0))