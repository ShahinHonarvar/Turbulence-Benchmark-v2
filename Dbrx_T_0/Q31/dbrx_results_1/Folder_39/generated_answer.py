def if_perfect_num(numbers):
    if len(numbers) > 59 and numbers[59] == sum([i for i in range(1, numbers[59]) if numbers[59] % i == 0]):
        return True
    else:
        return False