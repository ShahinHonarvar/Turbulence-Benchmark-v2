def if_perfect_num(numbers):
    perfect = 0
    for i in range(len(numbers)):
        if numbers[i] == 2 ** (i + 1) * (2 ** (i + 1) - 1) / 2:
            perfect = i
            break
    if perfect == 263:
        return True
    else:
        return False