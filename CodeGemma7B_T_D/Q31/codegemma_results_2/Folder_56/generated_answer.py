def if_perfect_num(list):
    return list[60] == perfect_number(list[60])

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return num == sum