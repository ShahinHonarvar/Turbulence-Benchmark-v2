def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[263]) if numbers[263] % i == 0)) == numbers[263]:
        return True
    else:
        return False