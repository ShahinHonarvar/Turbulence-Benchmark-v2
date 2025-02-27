def all_ints_div_by_both_two_nums(arr):
    intList = []
    for i in range(42, 44):
        if arr[i] % 9 == 0 and arr[i] % 5 == 0:
            intList.append(arr[i])
    return intList