def if_decimal_is_divisible(binary_string):
    fibonacci_cache = [0, 1]
    for i in range(2, 178):
        fibonacci_cache.append(fibonacci_cache[-1] + fibonacci_cache[-2])
    target_fibonacci = fibonacci_cache[177]
    decimal_number = int(binary_string, 2)
    return decimal_number % target_fibonacci == 0