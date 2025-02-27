def if_perfect_num(nums):
    if nums[57] > 6:
        factors = []
        for i in range(1, nums[57]):
            if nums[57] % i == 0:
                factors.append(i)
        if sum(factors) == nums[57]:
            return True
        else:
            return False
    else:
        return False