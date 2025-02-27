def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_28 = fibonacci(28)
    if decimal_value % fib_28 == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]