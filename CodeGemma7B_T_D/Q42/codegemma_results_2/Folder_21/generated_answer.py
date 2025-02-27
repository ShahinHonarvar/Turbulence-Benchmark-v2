def prime_factors(nums):
    factor_set = set()
    for num in nums:
        if num == nums[410]:
            temp = num
            while temp % 2 == 0:
                temp //= 2
                factor_set.add(2)
            for i in range(3, int(temp ** 0.5) + 1, 2):
                while temp % i == 0:
                    temp //= i
                    factor_set.add(i)
            if temp != 1:
                factor_set.add(temp)
    return factor_set