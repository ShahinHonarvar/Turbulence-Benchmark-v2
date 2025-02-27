def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[45], numbers[48])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[46:48])
    if missing_sum == 0:
        return ''
    hex_digits = '0123456789ABCDEF'
    if missing_sum % 2 == 0:
        hex_representation = []
        while missing_sum:
            missing_sum, remainder = divmod(missing_sum, 16)
            hex_representation.append(hex_digits[remainder])
        return ''.join(hex_representation[::-1]).upper()
    else:
        binary_representation = []
        while missing_sum:
            missing_sum, remainder = divmod(missing_sum, 2)
            binary_representation.append(str(remainder))
        return ''.join(binary_representation[::-1])