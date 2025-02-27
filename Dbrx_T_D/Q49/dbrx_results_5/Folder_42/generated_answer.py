def is_fibonacci(num):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(num - (phi ** num - psi ** num) / 5 ** 0.5) < 1e-10

def fibonacci_sequence(n):
    sequence = []
    a, b = (0, 1)
    for _ in range(n):
        sequence.append(a)
        a, b = (b, a + b)
    return sequence

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_nums = fibonacci_sequence(200)
    for i, num in enumerate(fibonacci_nums[:-1]):
        if num > decimal_num:
            break
        if decimal_num % fibonacci_nums[i + 1] == 0 and fibonacci_nums[i + 1] == 146:
            return True
    return False