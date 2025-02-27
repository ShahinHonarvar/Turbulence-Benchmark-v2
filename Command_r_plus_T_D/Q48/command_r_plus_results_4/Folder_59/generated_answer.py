def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[10])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[1:11]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    return bin(missing_sum) if missing_sum % 2 != 0 else hex(missing_sum)[2:].upper()