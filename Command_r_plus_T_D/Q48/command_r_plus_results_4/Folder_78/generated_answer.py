def return_binary_or_hexa(nums_tuple: tuple[int, ...]) -> str:
    sum_nums = 0
    for i in range(63, 97):
        if nums_tuple[i] not in nums_tuple[63:97]:
            sum_nums += nums_tuple[i]
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()
    return ''