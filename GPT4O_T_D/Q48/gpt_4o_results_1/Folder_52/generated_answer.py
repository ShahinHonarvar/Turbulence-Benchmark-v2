def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    sum_absent = sum((num for num in range(a + 1, b) if num not in numbers[38:82]))
    if sum_absent == 0:
        return ''
    return format(sum_absent, 'x') if sum_absent % 2 == 0 else format(sum_absent, 'b')