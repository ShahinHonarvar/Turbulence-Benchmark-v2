def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[23]) if numbers[23] % i == 0)) == numbers[23]:
        return True
    else:
        return False