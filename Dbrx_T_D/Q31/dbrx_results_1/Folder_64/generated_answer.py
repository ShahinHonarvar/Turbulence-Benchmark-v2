def if_perfect_num(numbers):
    if numbers[1] == sum((i for i in range(1, numbers[1]) if numbers[1] % i == 0)):
        return True
    else:
        return False