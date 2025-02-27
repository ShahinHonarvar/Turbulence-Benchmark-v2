def if_perfect_num(numbers):
    if len(numbers) > 10 and numbers[10] == sum([i for i in range(1, numbers[10]) if numbers[10] % i == 0]):
        return True
    else:
        return False