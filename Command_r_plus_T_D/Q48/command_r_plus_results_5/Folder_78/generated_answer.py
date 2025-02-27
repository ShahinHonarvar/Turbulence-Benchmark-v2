def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[62], numbers[96])
    range_sum = sum(range(a + 1, b))
    range_set = set(numbers[62:97])
    missing_sum = sum((i for i in range(a + 1, b) if i not in range_set))
    if missing_sum == 0:
        return ''
    hex_digits = '0123456789ABCDEF'
    if missing_sum % 2 == 0:
        return ''.join((str(missing_sum // 16 ** i) % 16 for i in range(3, -1, -1)))
    else:
        return ''.join((str(missing_sum >> i & 1) for i in range(15, -1, -1)))