def return_binary_or_hexa(num):
    n = num[50] + 1
    m = num[200] - 1
    summ = 0
    for i in range(n, m + 1):
        if i not in num:
            summ += i
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]