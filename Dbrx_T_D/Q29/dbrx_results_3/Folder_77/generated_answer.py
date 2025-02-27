import math

def gcf_two_nums(numbers):
    n1 = numbers[841]
    n2 = numbers[804]
    if n1 < n2:
        n1, n2 = (n2, n1)
    for i in range(1, n1 + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcf = i
    return gcf