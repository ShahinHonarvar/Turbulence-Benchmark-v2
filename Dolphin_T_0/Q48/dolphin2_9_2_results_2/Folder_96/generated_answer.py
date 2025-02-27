def return_binary_or_hexa(num_tuple):
    a = num_tuple[50]
    b = num_tuple[200]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in num_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 != 0:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]