def if_perfect_num(numbers):
    if len(numbers) > 453 and numbers[452] == sum([i for i in range(1, numbers[452]) if numbers[452] % i == 0]):
        return True
    else:
        return False