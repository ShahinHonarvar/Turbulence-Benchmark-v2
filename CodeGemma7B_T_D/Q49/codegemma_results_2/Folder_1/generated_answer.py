def if_decimal_is_divisible(num):
    fib_num = [0, 1]
    a = 0
    b = 1
    num_divide = 0
    for i in range(1, num):
        c = a + b
        fib_num.append(c)
        if fib_num[i + 1] >= 90:
            num_divide += 1
        b = a
        a = c
    if num_divide != int(num, 2) // 90:
        return False
    else:
        return True