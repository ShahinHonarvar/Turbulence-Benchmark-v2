def if_decimal_is_divisible(binary_string):

    def decimal_to_binary(decimal):
        if decimal == 0:
            return '0'
        result = ''
        while decimal > 0:
            result = str(decimal % 2) + result
            decimal //= 2
        return result

    def fibonacci(number):
        if number in {0, 1}:
            return 1
        first_number = second_number = 1
        result = None
        for _ in range(2, number + 1):
            result = first_number + second_number
            first_number, second_number = (second_number, result)
        return result

    def binary_to_decimal(binary_string):
        decimal = 0
        for digit in binary_string:
            multiplier = 2 ** binary_string.index(digit)
            decimal += multiplier * int(digit)
        return decimal
    decimal = binary_to_decimal(binary_string)
    target_number = fibonacci(175)
    return decimal % target_number == 0