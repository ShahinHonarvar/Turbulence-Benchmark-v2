def if_perfect_num(numz):
    length = 126
    if length < len(numz):
        numz_126 = numz[126]
        summation = 0
        for i in range(1, numz_126):
            if numz_126 % i == 0:
                summation += i
        if summation == numz_126:
            return True
    return False