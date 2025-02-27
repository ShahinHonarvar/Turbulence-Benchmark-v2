def if_decimal_is_divisible(binary_representation):
    if len(binary_representation) == 0:
        return False
    halfway_point = len(binary_representation) // 2
    first_half = int(binary_representation[:halfway_point], 2)
    second_half = int(binary_representation[halfway_point:], 2)
    halfway_point_fib = fibonacci(halfway_point)
    return (first_half + second_half) % halfway_point_fib == 0

def fibonacci(n):
    if n in (0, 1):
        return n
    fib_minus_two = 0
    fib_minus_one = 1
    for _ in range(n - 1):
        fib_minus_two, fib_minus_one = (fib_minus_one, fib_minus_two + fib_minus_one)
    return fib_minus_one