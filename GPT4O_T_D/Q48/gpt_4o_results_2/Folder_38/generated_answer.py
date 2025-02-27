def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    total_sum = 0
    nums_set = set(numbers[37:85])
    for num in range(a + 1, b):
        if num not in nums_set:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')