def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[8]
    all_integers = set(range(a + 1, b))
    present_integers = set(nums[4:8])
    missing_integers = all_integers - present_integers
    if not missing_integers:
        return ''
    total_sum = sum(missing_integers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]