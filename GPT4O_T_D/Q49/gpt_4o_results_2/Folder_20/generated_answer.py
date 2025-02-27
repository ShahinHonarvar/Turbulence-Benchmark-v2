def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 101):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    hundredth_fib = fibonacci[100]
    decimal_value = int(binary_string, 2)
    return decimal_value % hundredth_fib == 0