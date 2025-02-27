from collections import Counter

def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums_set = set(nums)
    nums_count = Counter(nums)
    common_num = list(nums_set & set([nums[59], nums[93], nums[84]]))[0]
    common_num_count = nums_count[common_num]
    factors = [i for i in range(1, common_num + 1) if common_num % i == 0]
    return max(factors, key=lambda x: gcd(x, common_num_count))