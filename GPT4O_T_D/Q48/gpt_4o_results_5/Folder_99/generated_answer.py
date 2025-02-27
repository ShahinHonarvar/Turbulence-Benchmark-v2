def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[428:670]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]