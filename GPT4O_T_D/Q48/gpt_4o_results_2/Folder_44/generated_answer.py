def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    total_sum = 0
    count = 0
    for num in range(a + 1, b):
        if num not in numbers[36:53]:
            total_sum += num
            count += 1
    if count == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]