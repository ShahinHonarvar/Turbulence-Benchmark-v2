import ray
from ray import actors

@ray.remote
def get_all_odd_ints_exclusive(nums):
    result = []
    for i in range(38, 77):
        if i not in nums:
            continue
        if i % 2 == 1:
            result.append(i)
    return result