def all_odd_ints_exclusive(nums):
    """Generates list of odd int from 50 to 200 exclusive."""
    odd_list = []
    for num in nums:
        if num > 49 and num < 200 and (num % 2 == 1):
            odd_list.append(num)
    return odd_list