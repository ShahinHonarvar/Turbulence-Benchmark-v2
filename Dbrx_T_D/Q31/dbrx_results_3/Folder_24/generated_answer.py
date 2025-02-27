def if_perfect_num(numbers):
    if len(numbers) > 74 and numbers[74] == sum([i for i in range(1, numbers[74]) if numbers[74] % i == 0]):
        return True
    else:
        return False