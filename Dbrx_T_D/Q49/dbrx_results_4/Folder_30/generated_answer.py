def if_decimal_is_divisible(binary_representation: str) -> bool:

    def is_divisible_by_fibonacci(number: int) -> bool:
        fibonacci = [0, 1]
        while fibonacci[-1] < number:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return number % fibonacci[-2] == 0
    decimal_number = int(binary_representation, 2)
    return is_divisible_by_fibonacci(decimal_number)