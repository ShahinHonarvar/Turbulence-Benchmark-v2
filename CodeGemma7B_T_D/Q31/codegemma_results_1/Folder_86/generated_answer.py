def if_perfect_num(arr):
    if arr[194] % sum([i for i in range(2, arr[194]) if arr[194] % i == 0]) == 0:
        return True
    return False