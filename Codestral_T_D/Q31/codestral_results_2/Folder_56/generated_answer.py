def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[60]) if numbers[60] % i == 0]) == numbers[60]:
        return True
    else:
        return False