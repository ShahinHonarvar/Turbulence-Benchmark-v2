import functools
import operator
import functools.reduce

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(functools.reduce, (functools.partial(operator.gcd, a=nums[66]), functools.partial(operator.gcd, a=nums[56]), functools.partial(operator.gcd, a=nums[92])), functools.partial(functools.reduce, operator.gcd))