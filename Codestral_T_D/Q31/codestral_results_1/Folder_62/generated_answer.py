def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[926]) if numbers[926] % i == 0)) == numbers[926]:
        return True
    return False