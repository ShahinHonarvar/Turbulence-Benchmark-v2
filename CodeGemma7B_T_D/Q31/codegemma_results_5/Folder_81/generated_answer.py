def if_perfect_num(a):
    if perfect_number(a[20]):
        return True
    else:
        return False

def perfect_number(a):
    sum = 0
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            sum += i + a // i
    if sum == a:
        return True
    else:
        return False