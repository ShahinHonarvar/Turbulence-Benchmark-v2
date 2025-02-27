def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[427], numbers[669])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(set(numbers[428:669]))
    if missing_sum == 0:
        return ''
    hex_digits = '0123456789ABCDEF'
    if missing_sum % 2 == 0:
        return ''.join((str(missing_sum // 16 ** i % 16) for i in range(4, -1, -1)))
    else:
        return ''.join((str(missing_sum >> i & 1) for i in range(missing_sum.bit_length() - 1, -1, -1)))