def if_perfect_num(numbers):
    if len(numbers) > 51 and numbers[51] == sum([i for i in range(1, numbers[51]) if numbers[51] % i == 0]):
        return True
    else:
        return False