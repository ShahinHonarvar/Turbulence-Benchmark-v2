def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[99]) if numbers[99] % i == 0]) == numbers[99]:
        return True
    else:
        return False