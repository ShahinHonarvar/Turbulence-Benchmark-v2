def if_perfect_num(numbers):
    if len(numbers) > 790 and numbers[790] == sum([i for i in range(1, numbers[790]) if numbers[790] % i == 0]):
        return True
    else:
        return False