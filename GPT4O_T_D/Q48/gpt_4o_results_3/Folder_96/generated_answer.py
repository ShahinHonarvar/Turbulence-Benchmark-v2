def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    number_set = set(numbers[51:200])
    missing_sum = sum((x for x in range(a + 1, b) if x not in number_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return f'{missing_sum:X}'
    else:
        return f'{missing_sum:b}'