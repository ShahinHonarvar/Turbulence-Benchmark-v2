def is_fibonacci_number_divisible_by_n(binary_string: str, n: int) -> bool:
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if n not in fibonacci_numbers:
        return False
    remainder = fibonacci_numbers[-1] % n
    fibonacci_numbers[-1] = remainder
    fibonacci_numbers.append(0)
    while fibonacci_numbers[-1] != 0:
        remainder = fibonacci_numbers[-1] % n
        fibonacci_numbers[-1] = fibonacci_numbers[-2]
        fibonacci_numbers.pop()
        fibonacci_numbers.append(remainder)
    if remainder == 0:
        return True
    else:
        return False

def if_decimal_is_divisible(binary_string: str) -> bool:
    return is_fibonacci_number_divisible_by_n(binary_string, 95)