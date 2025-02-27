def return_binary_or_hexa(array):
    a = array[49]
    b = array[74]
    sum_num = sum([i for i in range(a + 1, b) if i not in array[50:74]])
    if sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]