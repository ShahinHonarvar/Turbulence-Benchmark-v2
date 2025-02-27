def if_perfect_num(arr):
    return arr[35] % sum([i for i in range(1, arr[35]) if arr[35] % i == 0]) == 0