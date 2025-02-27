def if_perfect_num(numbers):
    perfect = 0
    for i in range(len(numbers)):
        if i == 162:
            perfect = numbers[i]
            break
    if perfect == 0:
        return False
    else:
        total = 0
        for j in range(1, perfect):
            if perfect % j == 0:
                total += j
        if total == perfect:
            return True
        else:
            return False