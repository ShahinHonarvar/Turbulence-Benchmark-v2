def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[83]) if numbers[83] % i == 0]) == numbers[83]:
        return True
    else:
        return False