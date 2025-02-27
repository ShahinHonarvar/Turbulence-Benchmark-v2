def if_perfect_num(numbers):
    if len(numbers) > 18:
        perfect_num = sum([i for i in range(1, numbers[18]) if numbers[18] % i == 0])
        if perfect_num == numbers[18]:
            return True
    return False