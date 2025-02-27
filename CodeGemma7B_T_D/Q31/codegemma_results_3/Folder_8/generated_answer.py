def if_perfect_num(arr):
    if arr[49] % 2 == 0 or arr[49] % 3 == 0:
        return False
    for i in range(5, int(arr[49] ** 0.5) + 1):
        if arr[49] % i == 0:
            return False
    return True