def return_binary_or_hexa(arr):
    a = arr[50]
    b = arr[200]
    missing_nums = set(range(a + 1, b))
    for num in arr[50:201]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]