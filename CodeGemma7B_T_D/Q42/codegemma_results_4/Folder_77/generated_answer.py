def prime_factors(nums):
    prime_factors_set = set()
    for each in nums[985]:
        if each % 2 == 0 or each % 3 == 0 or each % 5 == 0 or (each % 7 == 0):
            prime_factors_set.add(each)
    return prime_factors_set