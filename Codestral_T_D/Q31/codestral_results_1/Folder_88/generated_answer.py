def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[46]) if numbers[46] % i == 0]) == numbers[46]:
        return True
    else:
        return False