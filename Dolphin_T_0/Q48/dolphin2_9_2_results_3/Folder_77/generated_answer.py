def return_binary_or_hexa(arr):
    a, b = (arr[18], arr[52])
    missing = []
    for i in range(a + 1, b):
        i in arr[18:53] or missing.append(i)
    sum_ = sum(missing)
    if sum_ == 0 or sum_ % 2 == 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]