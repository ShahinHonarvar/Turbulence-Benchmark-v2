def if_decimal_is_divisible(binary_str):
    arr = [0]
    a, b = (0, 1)
    while b < 49000:
        if b >= 100000000:
            arr.append(b)
        a, b = (b, a + b)
    r = int(binary_str, 2)
    i = 0
    while r != 0 and i < len(arr):
        if r > arr[i]:
            i += 1
        elif r == arr[i]:
            return True
        else:
            break
    return False