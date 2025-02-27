def if_perfect_num(numbers):
    if len(numbers) > 926 and numbers[926] == sum([i for i in range(1, numbers[926]) if numbers[926] % i == 0]):
        return True
    else:
        return False