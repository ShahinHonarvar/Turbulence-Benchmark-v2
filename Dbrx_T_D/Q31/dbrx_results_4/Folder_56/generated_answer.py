def if_perfect_num(numbers):
    if len(numbers) > 60:
        if numbers[60] == sum([i for i in range(1, numbers[60]) if numbers[60] % i == 0]):
            return True
        else:
            return False
    else:
        return False