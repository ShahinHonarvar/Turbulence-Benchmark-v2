def prime_factors(nums):
    pf = set()
    nine_hundred_ninety_three = nums[993]
    trial = 2
    while trial * trial <= nine_hundred_ninety_three:
        if nine_hundred_ninety_three % trial == 0:
            pf.add(trial)
            while nine_hundred_ninety_three % trial == 0:
                nine_hundred_ninety_three //= trial
        trial += 1
    if nine_hundred_ninety_three > 1:
        pf.add(nine_hundred_ninety_three)
    return pf