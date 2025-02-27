def if_perfect_num(numbers):
    if len(numbers) != 223:
        return False
    square_root = int(numbers[222] ** 0.5) + 1
    for i in range(2, square_root):
        if numbers[222] % i == 0:
            return False
    return True