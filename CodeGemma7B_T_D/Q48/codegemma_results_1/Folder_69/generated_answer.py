def return_binary_or_hexa(lst):
    lst = sorted(lst)
    a = lst[39]
    b = lst[43]
    nums = set(range(a + 1, b))
    nums.difference_update(set(lst[39:44]))
    nums.add(0)
    sum = sum(nums)
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()