def if_perfect_num(numbers):
    if len(numbers) > 321 and numbers[321] > 0:
        perfect_num = [i for i in range(1, int(numbers[321] ** 0.5) + 1) if numbers[321] % i == 0]
        return sum(perfect_num[:-1]) * 2 == numbers[321]
    else:
        return False