def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_int = int(binary_representation, 2)
    fib_numbers = [0, 1]
    for _ in range(3, 161):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fib_160 = fib_numbers[160]
    return decimal_int % fib_160 == 0