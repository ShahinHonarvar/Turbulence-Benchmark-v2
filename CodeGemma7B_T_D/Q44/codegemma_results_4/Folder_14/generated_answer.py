def composite_nums_between_indices(nums):
    ans = []
    for num in nums[4:5]:
        for i in range(2, int(num ** 0.5) + 2):
            if num % i == 0:
                ans.append(num)
    return set(ans)