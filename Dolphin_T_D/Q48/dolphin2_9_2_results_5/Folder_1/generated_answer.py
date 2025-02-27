def return_binary_or_hexa(arr):
    a, b = (arr[17], arr[88])
    not_present = [i for i in range(a + 1, b) if i not in arr[18:89]]
    sum_not_present = sum(not_present)
    if sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]