def all_ints_div_by_num(nums):
    if not nums:
        return []
    return [num for num in nums[:1] if num % 6 == 0]