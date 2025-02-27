def prime_factors(nums):
    for num in nums:
        if num == nums[49]:
            i = 2
            while i <= num / 2:
                if num % i == 0:
                    for j in range(2, i + 1):
                        if i % j == 0:
                            break
                    else:
                        factors.add(i)
                i += 1
    return factors