from collections import defaultdict

def gcf_three_nums(nums):

    def gcd(pair):
        x, y = pair
        while y:
            x, y = (y, x % y)
        return x
    num1, num2, num3 = (nums[31], nums[69], nums[40])
    factors1 = defaultdict(int)
    factors2 = defaultdict(int)
    factors3 = defaultdict(int)
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors1[i] = 1
    for i in range(1, num2 + 1):
        for key in factors1.keys():
            if i * key in factors2:
                factors2[i * key] += 1
            elif i * key < num2 and num2 % (i * key) == 0:
                factors2[i * key] = 1
    for i in range(1, num3 + 1):
        for key in factors2.keys():
            if i * key in factors3:
                factors3[i * key] += 1
            elif i * key < num3 and num3 % (i * key) == 0:
                factors3[i * key] = 1
    common_factors = [key for key in factors3.keys() if factors3[key] == 3]
    return max(common_factors) if common_factors else 0