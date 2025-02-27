def if_perfect_num(lst):
    i = 6
    while i < len(lst):
        num = lst[i]
        if is_perfect_num(num):
            return True
        i += 6
    return False

def is_perfect_num(num):
    sum = 0
    for d in range(1, num):
        if num % d == 0:
            sum += d
    return sum == num