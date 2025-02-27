def if_perfect_num(numbers):
    if len(numbers) > 410:
        return numbers[410] == sum((i for i in range(1, numbers[410]) if numbers[410] % i == 0))
    return False