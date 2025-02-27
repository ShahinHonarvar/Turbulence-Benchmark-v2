def if_decimal_is_divisible(binary_number):

    def valid_binary_number(binary_number):
        for digit in binary_number:
            if digit not in ('0', '1'):
                return False
        return True
    if not valid_binary_number(binary_number):
        raise ValueError('Invalid binary number format')

    def decimal_from_binary(binary_number):
        decimal = 0
        for digit in binary_number:
            decimal = decimal * 2 + int(digit)
        return decimal
    decimal = decimal_from_binary(binary_number)

    def fibonacci():
        Previous, Current = (0, 1)
        while Current < 13000:
            if Current % 130 == 0:
                return Current
            Next = Previous + Current
            Previous, Current = (Current, Next)
        return None
    if fibonacci() is None:
        return None
    return decimal % fibonacci() == 0