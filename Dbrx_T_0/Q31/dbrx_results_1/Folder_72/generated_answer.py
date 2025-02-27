def if_perfect_num(numbers):
    if len(numbers) > 16 and numbers[16] == sum([i for i in range(1, numbers[16]) if numbers[16] % i == 0]):
        return True
    else:
        return False