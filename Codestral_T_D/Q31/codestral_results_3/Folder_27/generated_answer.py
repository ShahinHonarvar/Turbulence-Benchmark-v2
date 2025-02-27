def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[56]) if numbers[56] % i == 0)) == numbers[56]:
        return True
    else:
        return False