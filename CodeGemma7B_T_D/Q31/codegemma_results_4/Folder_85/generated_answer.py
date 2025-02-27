def if_perfect_num(l):
    return perfect_number(l[23])

def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n