def return_binary_or_hexa(x):
    a, b = x
    sum_ = 0
    for i in range(a + 1, b):
        if i not in x:
            sum_ += i
    return bin(sum_)[2:].zfill(len(str(bin(b - a + 1)[2:]))) if sum_ % 2 else hex(sum_)[2:].zfill(len(str(hex(b - a + 1)[2:]))) + '0'