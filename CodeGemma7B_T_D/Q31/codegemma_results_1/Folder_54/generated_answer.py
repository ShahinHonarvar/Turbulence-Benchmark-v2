def if_perfect_num(numbers):
    if numbers[51] % 2 == 0 and numbers[51] % 3 == 0 and (numbers[51] % 5 == 0) and (numbers[51] % 7 == 0) and (numbers[51] % 11 == 0):
        return True
    else:
        return False