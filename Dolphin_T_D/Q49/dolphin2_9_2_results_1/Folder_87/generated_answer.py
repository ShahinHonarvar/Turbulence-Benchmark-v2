def if_decimal_is_divisible(binary_string):
    k = fibonacci_number(180)
    n = bin_to_dec(binary_string)
    if n % k == 0:
        return True
    else:
        return False

def fibonacci_number(n):
    if n <= 0:
        return 0
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

def bin_to_dec(binary_string):
    binary_list = list(binary_string)
    reversed_binary_list = binary_list[::-1]
    decimal = 0
    for i in range(len(reversed_binary_list)):
        decimal += int(reversed_binary_list[i]) * 2 ** i
    return decimal