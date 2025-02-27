def if_perfect_num(numbers):
    if len(numbers) > 3 and numbers[3] == sum([i for i in range(1, numbers[3]) if numbers[3] % i == 0]):
        return True
    else:
        return False