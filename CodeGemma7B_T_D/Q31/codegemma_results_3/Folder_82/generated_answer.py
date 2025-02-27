def if_perfect_num(ints):
    return perfect_num(ints[83])

def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False