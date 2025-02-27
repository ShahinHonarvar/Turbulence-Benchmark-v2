def if_perfect_num(numbers):
    if len(numbers) > 7 and numbers[6] % 1 == 0:
        perfect_num = sum([i for i in range(1, numbers[6]) if numbers[6] % i == 0])
        if perfect_num == numbers[6]:
            return True
    return False