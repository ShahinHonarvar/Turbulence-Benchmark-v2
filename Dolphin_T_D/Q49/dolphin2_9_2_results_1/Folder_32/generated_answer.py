def fibonacci(n):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n + 1:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    return fibonacci_list[n]

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    return decimal % fibonacci(178) == 0