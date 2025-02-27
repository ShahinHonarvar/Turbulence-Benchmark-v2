def if_perfect_num(lst):
    if lst[64] == perfect_number(lst[64]):
        return True
    else:
        return False

def perfect_number(num):
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False