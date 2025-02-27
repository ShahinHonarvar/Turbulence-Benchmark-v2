def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    sum = 0
    not_in_tuple = True
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
        else:
            not_in_tuple = False
    if not_in_tuple:
        return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:]
    else:
        return ''