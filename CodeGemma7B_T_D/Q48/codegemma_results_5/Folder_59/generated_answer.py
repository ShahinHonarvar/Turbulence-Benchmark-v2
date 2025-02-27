def return_binary_or_hexa(tuple):
    a, *_, b = tuple
    sum = 0
    for num in range(a + 1, b):
        if num not in tuple:
            sum += num
    sum_str = str(sum)
    if sum % 2 == 0:
        return sum_str.zfill(len(sum_str))[-len(sum_str):].upper()
    else:
        return bin(sum)[2:].zfill(len(sum_str))[len(sum_str):].upper()