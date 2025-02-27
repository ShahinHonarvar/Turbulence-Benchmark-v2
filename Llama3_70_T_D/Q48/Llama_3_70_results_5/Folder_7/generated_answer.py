def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    s = set(numbers[10:98])
    total_sum = sum((i for i in range(a + 1, b) if i not in s))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]