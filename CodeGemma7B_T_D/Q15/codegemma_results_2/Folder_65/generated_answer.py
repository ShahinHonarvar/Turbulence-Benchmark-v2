def sum_odd_ints_inclusive(int_arr):
    sum = 0
    for num in range(56, 99):
        if num % 2 != 0:
            sum += int_arr[num]
    if sum == 0:
        return 0
    return sum