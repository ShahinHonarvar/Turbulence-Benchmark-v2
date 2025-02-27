def return_binary_or_hexa(num):
    num.sort()
    a = num[20]
    for i in num[21:52]:
        if a + 1 <= i <= num[-1]:
            num.remove(i)
    b = num[51]
    sum_ = 0
    for i in range(a + 1, b):
        sum_ += i
    if sum_ % 2:
        return '{0:b}'.format(sum_)
    else:
        return '{0:X}'.format(sum_)