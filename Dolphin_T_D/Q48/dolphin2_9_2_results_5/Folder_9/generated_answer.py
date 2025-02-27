def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    values = nums[71:200]
    if a != b - 1:
        summ = sum(set(range(a + 1, b)) - set(values))
        if summ % 2 == 0:
            return hex(summ)[2:].upper()
        else:
            return bin(summ)[2:]
    else:
        return ''