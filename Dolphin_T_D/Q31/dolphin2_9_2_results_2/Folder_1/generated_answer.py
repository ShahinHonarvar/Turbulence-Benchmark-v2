def if_perfect_num(numbers):
    if sum((div for div in range(1, numbers[85]) if numbers[85] % div == 0)) == numbers[85]:
        return True
    else:
        return False