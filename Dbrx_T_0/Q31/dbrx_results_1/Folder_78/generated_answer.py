def if_perfect_num(numbers):
    if len(numbers) > 91 and numbers[91] == sum([i for i in range(1, numbers[91]) if numbers[91] % i == 0]):
        return True
    else:
        return False