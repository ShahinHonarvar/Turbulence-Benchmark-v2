def if_perfect_num(li):
    if li[56] == perfect_num(li[56]):
        return True
    else:
        return False

def perfect_num(num):
    square = int(num ** 0.5)
    sum = 0
    for i in range(1, square + 1):
        if num % i == 0:
            sum += i
            sum += num // i
    return sum == num + 1