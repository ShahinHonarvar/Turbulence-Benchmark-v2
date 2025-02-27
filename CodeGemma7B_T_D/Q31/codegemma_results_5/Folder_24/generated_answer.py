def if_perfect_num(numbers):
    if numbers[74] % 6 == 0 and (numbers[74] - 1) % 3 not in [0, 1] and ((numbers[74] - 1) % 2 not in [0, 1]):
        return True
    else:
        return False