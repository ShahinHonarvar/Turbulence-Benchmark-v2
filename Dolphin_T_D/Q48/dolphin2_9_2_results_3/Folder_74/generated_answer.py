def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    not_in_list = [i for i in range(a + 1, b) if i not in numbers[70:97]]
    if len(not_in_list) == 0:
        return ''
    sum = 0
    for i in not_in_list:
        sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()