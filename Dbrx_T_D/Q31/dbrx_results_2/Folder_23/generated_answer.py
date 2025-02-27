def if_perfect_num(numbers):
    if len(numbers) > 69 and numbers[68] == sum([num for num in range(1, numbers[68]) if numbers[68] % num == 0]):
        return True
    else:
        return False