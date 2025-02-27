def if_decimal_is_divisible(binary_representation):
    fibonacci_cache = [0, 1]
    for i in range(2, 145):
        next_fib = fibonacci_cache[-1] + fibonacci_cache[-2]
        fibonacci_cache.append(next_fib)
    decimal_value = int(binary_representation, 2)
    return decimal_value % fibonacci_cache[144] == 0