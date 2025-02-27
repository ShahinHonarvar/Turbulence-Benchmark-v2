def if_perfect_num(numbers):
    if sum((1 for i in range(1, numbers[84]) if numbers[84] % i == 0)) == numbers[84]:
        return True
    else:
        return False