def if_decimal_is_divisible(arg):
    a, b = (1, 1)
    fib = 1
    fib_list = [1]
    while True:
        fib = a + b
        fib_list.append(fib)
        if fib >= 189:
            if str(fib)[-1] == '0' and int(str(fib)[-2]) % 2 == 0 and (int(str(fib)[-3]) % 2 != 0) and (int(str(fib)[-4]) % 2 != 0):
                temp = str(fib)[::-1]
                temp2 = int(temp)
                if int(temp) == temp2:
                    if int(arg) % int(temp2) == 0:
                        return True
                else:
                    b = fib
                    a = a + b - fib
        else:
            b = fib
            a = a + b - fib
    return False