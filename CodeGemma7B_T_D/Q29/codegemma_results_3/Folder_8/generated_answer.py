def gcf_two_nums(arr):
    a = arr[69]
    b = arr[41]
    while b:
        a, b = (b, a % b)
    return a