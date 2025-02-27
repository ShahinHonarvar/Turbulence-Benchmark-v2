def all_ints_div_by_both_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return abs(a)

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    target = lcm(-27, -96)
    return [i for i in nums[36:86] if i % target == 0]