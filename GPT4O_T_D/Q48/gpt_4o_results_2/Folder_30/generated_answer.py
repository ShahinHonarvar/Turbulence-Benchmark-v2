def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    sum_missing = 0
    found_missing = False
    for number in range(a + 1, b):
        if number not in numbers[23:25]:
            sum_missing += number
            found_missing = True
    if not found_missing:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]