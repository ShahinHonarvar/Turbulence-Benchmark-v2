def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) < 201:
        return set()
    composite_set = set()
    for index in range(20, 201):
        num = nums[index]
        if is_composite(num):
            composite_set.add(num)
    return composite_set