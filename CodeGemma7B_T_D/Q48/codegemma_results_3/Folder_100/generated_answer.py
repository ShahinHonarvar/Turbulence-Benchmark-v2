def return_binary_or_hexa(t):
    sum = 0
    for i in range(t[44] + 1, t[78]):
        if i not in t:
            sum += i
    return format(sum, 'b') if sum % 2 else format(sum, 'x')