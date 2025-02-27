import math

def gcf_three_nums(nums):
    element1 = nums[44]
    element2 = nums[91]
    element3 = nums[42]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def factorize(num):
        factors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(int(num / i))
        return set(factors)
    el1_factors = factorize(element1)
    el2_factors = factorize(element2)
    el3_factors = factorize(element3)
    common_factors = list(el1_factors & el2_factors & el3_factors)
    return max(common_factors)