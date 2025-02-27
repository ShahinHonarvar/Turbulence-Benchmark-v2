def all_odd_ints_exclusive(nums):
    evens = []
    for num in nums[3:8]:
        if num % 2 == 1:
            evens.append(num)
    if len(evens) == 0:
        return []