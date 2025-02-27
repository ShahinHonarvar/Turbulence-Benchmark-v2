def return_binary_or_hexa(numbers):
    a, b = (numbers[1], numbers[8])
    missing = [x for x in range(a + 1, b) if x not in numbers[1:8]]
    if len(missing) == 0:
        return ''
    else:
        sum_ = sum(missing)
        return bin(sum_).replace('0b', '') if sum_ % 2 != 0 else hex(sum_).replace('0x', '')