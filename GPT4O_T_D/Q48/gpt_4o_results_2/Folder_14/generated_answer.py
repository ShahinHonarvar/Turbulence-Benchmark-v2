def return_binary_or_hexa(numbers):
    if len(numbers) <= 5:
        return ''
    a = numbers[2]
    b = numbers[5]
    total_sum = 0
    all_present = True
    for i in range(a + 1, b):
        if i not in numbers[3:5]:
            total_sum += i
            all_present = False
    if all_present:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]