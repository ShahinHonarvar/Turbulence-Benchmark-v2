def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fib_cache = [0, 1]
    for i in range(2, 78):
        fib_cache.append(fib_cache[-1] + fib_cache[-2])
    return n % fib_cache[77] == 0