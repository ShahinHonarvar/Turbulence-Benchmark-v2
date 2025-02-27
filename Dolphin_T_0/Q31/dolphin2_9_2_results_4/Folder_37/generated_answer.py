def if_perfect_num(array):
    if len(array) > 28:
        number = array[28]
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        if sum == number:
            return True
        else:
            return False
    else:
        return False