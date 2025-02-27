def if_perfect_num(numbers):
    if len(numbers) > 17:
        n = numbers[17]
        return sum((i for i in range(1, n) if n % i == 0)) == n
    else:
        return False