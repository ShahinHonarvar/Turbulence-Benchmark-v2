def if_perfect_num(numbers):
    if len(numbers) > 37 and numbers[37] > 0 and (numbers[37] == 1 or (numbers[37] % 2 == 0 and sum((num for num in range(1, numbers[37]) if numbers[37] % num == 0)) == numbers[37]) or (numbers[37] % 2 != 0 and sum((num for num in range(1, numbers[37], 2) if numbers[37] % num == 0)) == numbers[37])):
        return True
    else:
        return False