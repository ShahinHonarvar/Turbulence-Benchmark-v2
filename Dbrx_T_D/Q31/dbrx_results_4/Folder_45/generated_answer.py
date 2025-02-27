def if_perfect_num(integers):
    if len(integers) > 33 and is_perfect(integers[33]):
        return True
    else:
        return False

def is_perfect(number):
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
    return sum == number