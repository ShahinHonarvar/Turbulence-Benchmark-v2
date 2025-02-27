def all_pos_ints_exclusive(nums):
    if any((n > 0 and index in range(86, 91) for n, index in enumerate(nums))):
        return [n for n in nums if n > 0 and index in range(86, 91)]
    else:
        return []