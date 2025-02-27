def return_binary_or_hexa(arr):
    a = arr[20]
    b = arr[35]
    arr2 = arr[21:36]
    ints = set()
    for i in arr2:
        ints.add(i)
    s = 0
    for i in range(a + 1, b + 1):
        if not i in ints:
            s += i
    if s % 2 == 0:
        s = hex(s).lstrip('0x')
    else:
        s = bin(s).lstrip('0b')
    return s