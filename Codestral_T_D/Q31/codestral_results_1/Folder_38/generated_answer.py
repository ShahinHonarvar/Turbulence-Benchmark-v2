def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[38]) if numbers[38] % i == 0]) == numbers[38]:
        return True
    else:
        return False