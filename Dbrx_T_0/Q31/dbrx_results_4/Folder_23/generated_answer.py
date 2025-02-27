def if_perfect_num(numbers):
    if len(numbers) > 69 and numbers[68] == sum([i for i in range(1, numbers[68]) if numbers[68] % i == 0]):
        return True
    else:
        return False