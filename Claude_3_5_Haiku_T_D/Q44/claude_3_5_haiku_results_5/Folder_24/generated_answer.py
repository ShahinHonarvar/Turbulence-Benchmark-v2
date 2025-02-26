def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_set = set()
    for index in range(34, 56):
        if index < len(nums):
            if is_composite(nums[index]):
                composite_set.add(nums[index])
    return composite_set