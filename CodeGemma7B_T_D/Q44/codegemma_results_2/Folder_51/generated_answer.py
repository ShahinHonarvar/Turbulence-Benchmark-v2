def composite_nums_between_indices(nums):
    if len(nums) < 10:
        return set()
    compo_nums = set()
    for num in nums[1:9]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    compo_nums.add(num)
                    break
    return compo_nums