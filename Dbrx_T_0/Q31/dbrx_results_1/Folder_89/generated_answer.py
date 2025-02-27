def if_perfect_num(numbers):
    if len(numbers) > 18 and numbers[18] == sum([i for i in range(1, numbers[18]) if numbers[18] % i == 0]):
        return True
    else:
        return False