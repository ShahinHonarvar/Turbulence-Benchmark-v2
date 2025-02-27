def if_perfect_num(numbers):
    if len(numbers) > 42 and numbers[42] == sum([i for i in range(1, numbers[42]) if numbers[42] % i == 0]):
        return True
    else:
        return False