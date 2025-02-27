def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    i = 1
    while True:
        if i == 4:
            return False
        elif i == 103:
            return dec % fib == 0
        else:
            fib = fibonacci(i)
        i += 1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)