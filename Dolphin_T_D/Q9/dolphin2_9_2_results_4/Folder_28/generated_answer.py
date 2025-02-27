def all_odd_ints_inclusive(arr):
    odd_nums = []
    for num in arr[62:64]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums