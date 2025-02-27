def if_decimal_is_divisible(binary_str):
    fibonacci_cache = [0, 1]
    for i in range(2, 129):
        fibonacci_cache.append(fibonacci_cache[i - 1] + fibonacci_cache[i - 2])
    fibonacci_number = fibonacci_cache[127]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_number == 0