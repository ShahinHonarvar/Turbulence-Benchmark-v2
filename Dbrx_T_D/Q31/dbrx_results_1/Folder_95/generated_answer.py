def if_perfect_num(numbers):
    if len(numbers) > 87 and numbers[87] > 0:
        perfect_num = sum([i for i in range(1, numbers[87]) if numbers[87] % i == 0])
        return perfect_num == numbers[87]
    else:
        return False