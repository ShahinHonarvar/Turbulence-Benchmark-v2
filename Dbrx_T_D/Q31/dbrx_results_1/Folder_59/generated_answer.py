def if_perfect_num(numbers):
    if len(numbers) < 3:
        return False
    perfect_num = 0
    for i in range(1, int(numbers[2]) + 1):
        if numbers[2] % i == 0:
            perfect_num += i
    if perfect_num == numbers[2]:
        return True
    return False