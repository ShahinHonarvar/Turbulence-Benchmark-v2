def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    total = 0
    nums_set = set(numbers[70:97])
    for n in range(a + 1, b):
        if n not in nums_set:
            total += n
    if total == 0:
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]