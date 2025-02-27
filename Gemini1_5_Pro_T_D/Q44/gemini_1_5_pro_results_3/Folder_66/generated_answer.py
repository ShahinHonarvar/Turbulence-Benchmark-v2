def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(0, len(nums) - 1)):
        n = nums[i]
        if 62 <= i <= 63 and (n <= 1 or any((n % j == 0 for j in range(2, int(n ** 0.5) + 1)))):
            result.add(n)
    return result