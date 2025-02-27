from itertools import count

def composite_nums_between_indices(nums):
    composites = set((n for n in nums[69:84] if not all((n % i for i in range(2, n)))))
    return composites if composites else set()