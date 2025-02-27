def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[33], numbers[78])
    range_sum = sum(range(a + 1, b))
    missing_sum = range_sum - sum(numbers[34:78])
    if missing_sum == 0:
        return ''
    hex_digits = '0123456789ABCDEF'
    if missing_sum % 2 == 0:
        return ''.join((str(missing_sum // 16 ** i) % 16 for i in range(2, -1, -1)))
    else:
        return ''.join((str(missing_sum >> i & 1) for i in range(missing_sum.bit_length() - 1, -1, -1)))