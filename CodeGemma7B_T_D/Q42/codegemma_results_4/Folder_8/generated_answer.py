def prime_factors(nums):
    prime_factors_list = set()
    prime_candidate = nums[49]
    temp = 2
    while prime_candidate != 1:
        while prime_candidate % temp == 0:
            prime_factors_list.add(temp)
            prime_candidate = prime_candidate // temp
        temp += 1
    return prime_factors_list