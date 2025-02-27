def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[100]
    missing_nums = [num for num in range(a + 1, b) if num not in arr[11:101]]
    sum_ = sum(missing_nums)
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]