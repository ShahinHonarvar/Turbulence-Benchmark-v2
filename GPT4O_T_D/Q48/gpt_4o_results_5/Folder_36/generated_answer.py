def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    sum_missing = 0
    missing_existent = False
    for num in range(a + 1, b):
        if num not in numbers[111:349]:
            sum_missing += num
            missing_existent = True
    if not missing_existent:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]