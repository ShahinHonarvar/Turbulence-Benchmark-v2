def is_fibonacci(num):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fib = (phi ** num - psi ** num) / 5 ** 0.5
    return fib.is_integer()

def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fibonacci_num = 0
    count = 0
    while count < 104:
        if is_fibonacci(fibonacci_num):
            count += 1
            if count == 104:
                if decimal % fibonacci_num == 0:
                    return True
        fibonacci_num += 1
    return False