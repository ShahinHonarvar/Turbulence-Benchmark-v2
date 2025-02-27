def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[96]) if numbers[96] % i == 0)) == numbers[96]:
        return True
    return False