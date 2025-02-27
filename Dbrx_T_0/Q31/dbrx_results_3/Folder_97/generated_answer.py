def if_perfect_num(numbers):
    if len(numbers) > 132 and numbers[132] == sum([i for i in range(1, numbers[132]) if numbers[132] % i == 0]):
        return True
    else:
        return False