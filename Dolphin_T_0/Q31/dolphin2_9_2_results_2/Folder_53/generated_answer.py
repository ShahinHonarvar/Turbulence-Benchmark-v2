def if_perfect_num(numbers):
    if sum((numbers[i] * 1 for i in range(1, int(numbers[73] ** 0.5 + 1)) if numbers[73] % i == 0)) * 2 == numbers[73]:
        return True
    else:
        return False