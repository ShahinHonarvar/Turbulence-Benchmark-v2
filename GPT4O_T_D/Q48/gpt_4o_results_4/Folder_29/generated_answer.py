def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    present_numbers = set(numbers[71:98])
    needed_sum = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if needed_sum == 0:
        return ''
    if needed_sum % 2 == 1:
        return format(needed_sum, 'b')
    else:
        return format(needed_sum, 'x')