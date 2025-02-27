def is_fibonacci(n):
    return (5 * n * n - 4) % (n - 1) == 0

def fibonacci_position(n):
    if n == 0 or n == 1:
        return n
    a, b = (0, 1)
    pos = 2
    while b < n:
        a, b = (b, a + b)
        pos += 1
    return pos

def bin_to_dec(bin_str):
    return int(bin_str, 2)

def if_decimal_is_divisible(bin_str):
    dec = bin_to_dec(bin_str)
    fib_pos = fibonacci_position(dec)
    fib_num = 0
    for i in range(fib_pos):
        if i == 0 or i == 1:
            fib_num = i
        else:
            fib_num = fib_num + fib_num
    return dec % fib_num == 0