def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[702]) if numbers[702] % i == 0)) == numbers[702]:
        return True
    else:
        return False