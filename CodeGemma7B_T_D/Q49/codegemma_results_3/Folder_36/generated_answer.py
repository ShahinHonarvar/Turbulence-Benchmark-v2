def if_decimal_is_divisible(binary_string):

    def get_fibonacci_term(term):
        if term < 2:
            return term
        return get_fibonacci_term(term - 1) + get_fibonacci_term(term - 2)

    def get_decimal_value(byte_array):
        return int(''.join(map(str, byte_array)), 2)
    byte_array = []
    for i in range(0, len(binary_string), 8):
        byte_array.append(int(binary_string[i:i + 8], 2))
    term = 1
    fibonacci_term = get_fibonacci_term(term)
    while fibonacci_term < get_decimal_value(byte_array):
        term += 1
        fibonacci_term = get_fibonacci_term(term)
    return term <= 149