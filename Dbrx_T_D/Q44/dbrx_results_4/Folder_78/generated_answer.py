def composite_nums_between_indices(nums):
    composite_numbers = set(filter(lambda x: x > 1 and x % 2 != 0 and (x % 3 != 0) and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1))), nums))
    return set(composite_numbers).intersection(set(nums[70:85]))