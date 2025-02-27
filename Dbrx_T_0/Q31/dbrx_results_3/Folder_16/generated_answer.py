def if_perfect_num(numbers):
    if len(numbers) > 162 and numbers[162] == sum([i for i in range(1, numbers[162]) if numbers[162] % i == 0]):
        return True
    else:
        return False