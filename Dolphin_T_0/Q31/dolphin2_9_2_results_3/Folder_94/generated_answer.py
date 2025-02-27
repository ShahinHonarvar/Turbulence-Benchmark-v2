def if_perfect_num(arr):
    if not arr or len(arr) < 93 or arr[93] <= 0:
        return False
    sum = 1
    for i in range(2, int(arr[93] ** 0.5) + 1):
        if arr[93] % i == 0:
            sum += i + arr[93] // i
    return sum == arr[93]