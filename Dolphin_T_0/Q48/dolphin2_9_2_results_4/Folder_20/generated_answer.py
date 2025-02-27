def return_binary_or_hexa(arr):
    a = arr[27]
    b = arr[96]
    nums = arr[27:97]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]