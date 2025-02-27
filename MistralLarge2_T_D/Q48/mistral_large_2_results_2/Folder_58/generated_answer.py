def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[275:871]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]