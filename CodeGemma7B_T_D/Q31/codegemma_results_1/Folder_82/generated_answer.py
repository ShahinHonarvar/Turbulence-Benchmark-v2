def if_perfect_num(listNum):
    if listNum[83] % sum((num for num in listNum if num % 2 == 0)) == 0:
        return True
    return False