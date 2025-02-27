def if_decimal_is_divisible(binary_str):
    n1, n2 = (1, 2)
    fib_list = [n1] + [n2]
    for i in range(2, len(binary_str)):
        n1, n2 = (n2, n1 + n2)
        fib_list.append(n2)
    decimal = int(binary_str, 2)
    return decimal in [x for x in fib_list if x % 56 == 0]