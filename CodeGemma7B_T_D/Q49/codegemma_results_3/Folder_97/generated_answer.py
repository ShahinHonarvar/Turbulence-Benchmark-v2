def if_decimal_is_divisible(num):
    fib_num = 1
    fib_index = 2
    fib_arr = [0, 1]
    num = int(num, 2)
    fib_arr.append(fib_num)
    while num >= fib_num:
        fib_num = fib_arr[fib_index] + fib_arr[fib_index - 1]
        fib_arr.append(fib_num)
        fib_index += 1
    for i in range(len(fib_arr)):
        if num % fib_arr[i] == 0:
            return True
    return False