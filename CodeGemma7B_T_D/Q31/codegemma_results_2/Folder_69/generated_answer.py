def if_perfect_num(l):
    if l[459] % perfect_num(l[459]):
        return True
    else:
        return False

def perfect_num(n):
    temp = 0
    for i in range(1, n):
        if n % i == 0:
            temp += i
    if temp == n:
        return True
    else:
        return False