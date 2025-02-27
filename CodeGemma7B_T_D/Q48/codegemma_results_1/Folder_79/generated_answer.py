def return_binary_or_hexa(a_b):
    sum = 0
    for i in range(a_b[1] + 1, a_b[7]):
        if i not in a_b[1:7]:
            sum += i
    if sum % 2 != 0:
        return f'{sum:b}'
    else:
        return f'{sum:x}'