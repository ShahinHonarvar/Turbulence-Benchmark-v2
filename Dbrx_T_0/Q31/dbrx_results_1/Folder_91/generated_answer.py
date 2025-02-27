def if_perfect_num(numbers):
    if len(numbers) > 6 and numbers[6] == sum([i for i in range(1, numbers[6]) if numbers[6] % i == 0]):
        return True
    else:
        return False