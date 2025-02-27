def return_binary_or_hexa(arr):
    a = arr[2]
    b = arr[8]
    sum = 0
    for i in range(a + 1, b + 1):
        if i not in arr[3:9]:
            sum += i
    ret = ''
    if sum % 2 == 1:
        ret = str(bin(sum))[2:]
    else:
        ret = hex(sum)[2:]
    if ret == '':
        return ''
    else:
        return ret