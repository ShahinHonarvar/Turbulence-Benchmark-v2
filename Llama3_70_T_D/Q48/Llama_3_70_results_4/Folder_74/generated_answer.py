def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    missing_nums = [i for i in range(a + 1, b) if i not in t[70:98]]
    num_sum = sum(missing_nums)
    if num_sum % 2 == 1:
        return bin(num_sum)[2:]
    elif num_sum != 0:
        return hex(num_sum)[2:]
    else:
        return ''