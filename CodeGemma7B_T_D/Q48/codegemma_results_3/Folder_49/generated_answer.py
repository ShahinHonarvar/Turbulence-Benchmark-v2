def return_binary_or_hexa(arr):
    low = arr[81]
    high = arr[199]
    sum = 0
    for i in range(low, high + 1):
        if i not in arr[81:200]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()