def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[0]) if numbers[0] % i == 0]) == numbers[0]:
        return True
    else:
        return False