def binary_representation(n):
    return format(n, '08b')[-8:]

def hex_representation(n):
    return format(n, 'x')

def is_even(n):
    return n % 2 == 0

def calculate_sum(t):
    a = t[10]
    b = t[12]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[10:13]:
            sum += i
    return sum

def return_binary_or_hexa(t):
    sum = calculate_sum(t)
    if is_even(sum):
        return hex_representation(sum)
    else:
        return binary_representation(sum)