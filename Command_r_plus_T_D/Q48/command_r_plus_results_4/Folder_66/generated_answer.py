def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[75])
    range_sum = sum(range(a + 1, b))
    missing_sum = range_sum - sum(numbers[11:76])
    if missing_sum == 0:
        return ''
    hex_digits = '0123456789ABCDEF'
    if missing_sum % 2 == 0:
        return ''.join((str(missing_sum // 16 ** i % 16) for i in range(4, -1, -1)))
    else:
        return ''.join((str(missing_sum >> i & 1) for i in range(10, -1, -1)))