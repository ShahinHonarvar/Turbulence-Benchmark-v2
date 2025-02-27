def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = [0, 1]
    while True:
        next_fibonacci_number = fibonacci_number[-1] + fibonacci_number[-2]
        if next_fibonacci_number > decimal_number // 2:
            break
        fibonacci_number.append(next_fibonacci_number)
    for num in fibonacci_number:
        if decimal_number % num == 0:
            return True
    return False