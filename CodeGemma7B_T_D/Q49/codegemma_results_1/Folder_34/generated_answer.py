def if_decimal_is_divisible(binary_representation):
    fib_num = 0
    fibonacci_list = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    for i in range(len(binary_representation)):
        if binary_representation[i] == '1':
            fib_num += 2 ** (len(binary_representation) - i - 1)
    if fib_num in fibonacci_list:
        index = fibonacci_list.index(fib_num)
        i = 24 - index
        if fibonacci_list[i] % 24 == 0 or fibonacci_list[i] % 24 == 1 or fibonacci_list[i] % 24 == 23:
            return True
    return False