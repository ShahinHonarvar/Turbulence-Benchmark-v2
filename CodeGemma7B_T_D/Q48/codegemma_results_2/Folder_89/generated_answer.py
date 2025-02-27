def return_binary_or_hexa(num):
    a = num[55]
    b = num[84]
    total_sum = 0
    for i in range(a + 1, b):
        if num.count(i) == 0:
            total_sum += i
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')