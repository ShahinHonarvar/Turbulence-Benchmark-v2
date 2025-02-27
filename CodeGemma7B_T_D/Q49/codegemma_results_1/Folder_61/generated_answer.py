def if_decimal_is_divisible(binary_str):

    def get_formatted_binary_str(binary_str):
        return ''.join((binary_str[i:i + 4] for i in range(0, len(binary_str), 4)))

    def find_76th_fibonacci_number(formatted_binary_str):
        a, b = (int(formatted_binary_str[0], 2), int(formatted_binary_str[1], 2))
        for i in range(2, 76):
            a, b = (b, a + b)
        return b
    formatted_binary_str = get_formatted_binary_str(binary_str)
    return find_76th_fibonacci_number(formatted_binary_str) % 76 == 0