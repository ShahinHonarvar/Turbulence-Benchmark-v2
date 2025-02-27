def if_perfect_num(numbers):
    if len(numbers) > 57 and numbers[57] == sum([i for i in range(1, numbers[57]) if numbers[57] % i == 0]):
        return True
    else:
        return False