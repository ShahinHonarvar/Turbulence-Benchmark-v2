def return_binary_or_hexa(t):
    a, b = (t[20], t[36])
    missing_nums = [num for num in range(a + 1, b) if num not in t[20:37]]
    result_sum = sum(missing_nums)
    if result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]