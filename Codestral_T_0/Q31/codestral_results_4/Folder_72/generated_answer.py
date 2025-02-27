def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[16]) if numbers[16] % i == 0)) == numbers[16]:
        return True
    else:
        return False