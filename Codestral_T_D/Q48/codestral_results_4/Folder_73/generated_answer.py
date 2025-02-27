def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    missing_nums = [i for i in range(a + 1, b) if i not in t[10:77]]
    num_sum = sum(missing_nums)
    if num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:]
    if not missing_nums:
        return ''