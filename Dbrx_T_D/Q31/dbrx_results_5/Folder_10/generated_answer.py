def if_perfect_num(numbers):
    if len(numbers) > 54 and numbers[54] == sum([i for i in range(1, numbers[54]) if numbers[54] % i == 0]):
        return True
    else:
        return False