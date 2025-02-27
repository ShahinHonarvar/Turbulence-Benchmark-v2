def if_decimal_is_divisible(binary):
    fib_div = len([num for num in fibonacci(binary) if num % 6 == 0])
    return True if fib_div > 0 else False

def fibonacci(binary):
    fib = [0, 1]
    num = int(binary, 2)
    while num > fib[-1]:
        fib.append(fib[-1] + fib[-2])
    return fib