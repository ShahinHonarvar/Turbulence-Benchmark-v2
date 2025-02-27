def if_decimal_is_divisible(binary_str):
    fib_num = 0
    index = 0
    temp = 0
    if len(binary_str) > 0:
        for i in range(len(binary_str) - 1, -1, -1):
            num = int(binary_str[i])
            fib_num = (fib_num + temp) * 2 + num
            temp = num
            index += 1
            if index == len(binary_str):
                fib_num += 1
            if fib_num % 19 == 0 and index != 0:
                return True
    return False