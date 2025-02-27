def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 100 == 0

def find_fibonacci_position(n):
    return (math.log(n * math.sqrt(5) + 0.5) - math.log(0.5)) // math.log((1 + math.sqrt(5)) / 2)

def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    if is_fibonacci(decimal_num):
        return find_fibonacci_position(decimal_num) >= 118
    else:
        return False