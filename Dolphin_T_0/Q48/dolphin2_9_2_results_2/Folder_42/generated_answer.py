def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    numbers_between = [num for num in range(a + 1, b) if num not in t]
    if not numbers_between:
        return ''
    sum_of_numbers = sum(numbers_between)
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]