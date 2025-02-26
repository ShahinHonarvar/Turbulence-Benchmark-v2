def return_binary_or_hexa(arr):
    a = arr[38]
    b = arr[81]
    missing_nums = [num for num in range(a + 1, b) if num not in arr[38:82]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]