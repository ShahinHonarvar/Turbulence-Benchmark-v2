def if_perfect_num(numbers):
    if len(numbers) > 48 and numbers[48] == sum([i for i in range(1, numbers[48]) if numbers[48] % i == 0]):
        return True
    else:
        return False