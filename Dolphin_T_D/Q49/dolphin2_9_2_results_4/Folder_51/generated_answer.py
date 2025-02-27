def if_decimal_is_divisible(binary_string):
    binary_list = [int(x) for x in binary_string]
    binary_list.reverse()
    n = 0
    for i in range(len(binary_list)):
        n += binary_list[i] * 2 ** i
    fibonacci_list = [0, 1]
    for i in range(2, 17):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    fibonacci_number = fibonacci_list[16]
    if n % fibonacci_number == 0:
        return True
    else:
        return False