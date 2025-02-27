def fibonacci_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

def binary_to_int(binary_string):
    decimal = 0
    for char in binary_string:
        decimal = decimal * 2 + int(char)
    return decimal

def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = fibonacci_sequence(35)
    decimal = binary_to_int(binary_string)
    return decimal % fibonacci_numbers[34] == 0