def if_perfect_num(l):
    return perfect_number(l[790])

def perfect_number(num):
    sum_factor = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_factor += i
    return sum_factor == num