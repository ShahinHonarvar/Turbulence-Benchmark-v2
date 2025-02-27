def if_perfect_num(numbers):
    if len(numbers) > 88 and numbers[88] > 0:
        perfect_number = [num for num in range(1, numbers[88]) if numbers[88] % num == 0]
        return sum(perfect_number) == numbers[88]
    else:
        return False