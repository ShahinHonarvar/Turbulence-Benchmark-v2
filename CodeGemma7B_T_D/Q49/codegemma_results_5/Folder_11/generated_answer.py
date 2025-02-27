def if_decimal_is_divisible(binary_representation):

    def binary_to_decimal(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal

    def is_divisible_by_fibonacci(number):
        fibonacci_numbers = [0]
        a, b = (0, 1)
        while b <= number:
            fibonacci_numbers.append(b)
            a, b = (b, a + b)
        return number in fibonacci_numbers and fibonacci_numbers.index(number) >= 15
    decimal = binary_to_decimal(binary_representation)
    return is_divisible_by_fibonacci(decimal)