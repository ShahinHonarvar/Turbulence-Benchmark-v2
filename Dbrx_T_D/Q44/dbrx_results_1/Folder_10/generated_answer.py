def composite_nums_between_indices(nums):
    composite_nums = set(filter(lambda x: x > 1 and all((x % y != 0 for y in range(2, int(x ** 0.5) + 1))), nums))
    return set((enum[1] for enum in enumerate(nums) if 37 <= enum[0] <= 51)) & composite_nums