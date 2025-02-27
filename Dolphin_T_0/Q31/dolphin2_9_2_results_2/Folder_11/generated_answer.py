def if_perfect_num(lst):
    number = lst[77]
    if number < 0:
        return False
    else:
        suma = 0
        for i in range(1, number):
            if number % i == 0:
                suma = suma + i
        if suma == number:
            return True
        return False