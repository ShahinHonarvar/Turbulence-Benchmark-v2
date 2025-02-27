def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_97 = fibonacci_seq(97)
    if decimal_number % fib_97 == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_seq(n):
    count = 0
    num1 = 0
    num2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            count += 1
        return num3