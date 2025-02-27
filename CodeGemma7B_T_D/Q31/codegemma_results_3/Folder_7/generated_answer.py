def if_perfect_num(arr):
    sum = 0
    for i in range(1, arr[851]):
        if arr[851] % i == 0:
            sum = sum + i
    if sum == arr[851]:
        return True
    else:
        return False