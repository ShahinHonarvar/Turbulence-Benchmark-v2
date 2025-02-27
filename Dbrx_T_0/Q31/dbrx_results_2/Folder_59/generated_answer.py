def if_perfect_num(numbers):
    if len(numbers) < 3:
        return False
    perfect_num = 0
    for i in range(1, numbers[2]):
        if numbers[2] % i == 0:
            perfect_num += i
    return perfect_num == numbers[2]