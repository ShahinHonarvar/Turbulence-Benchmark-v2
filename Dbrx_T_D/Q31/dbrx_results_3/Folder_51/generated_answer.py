def if_perfect_num(numbers):
    if len(numbers) > 64 and numbers[63] == sum([i for i in range(1, numbers[63]) if numbers[63] % i == 0]):
        return True
    else:
        return False