def if_perfect_num(numbers):
    if len(numbers) > 632 and numbers[632] == sum([i for i in range(1, numbers[632]) if numbers[632] % i == 0]):
        return True
    else:
        return False