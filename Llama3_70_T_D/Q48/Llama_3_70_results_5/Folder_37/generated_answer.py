def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[2:8]:
            total_sum += i
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]