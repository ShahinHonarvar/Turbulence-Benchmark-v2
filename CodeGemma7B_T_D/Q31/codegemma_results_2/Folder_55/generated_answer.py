def if_perfect_num(arr):
    d = {key: value for key, value in enumerate(arr) if key % 2 == 0 and value % 2 == 0}
    sum_d = sum(d.values())
    return sum_d == arr[21]