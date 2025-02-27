def if_perfect_num(arr):
    if arr[3] % 2 == 0 or arr[3] % 3 == 0 or arr[3] % 5 == 0:
        return True
    else:
        return False