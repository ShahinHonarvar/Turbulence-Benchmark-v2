def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return abs(a)

    def lcm(a, b):
        return abs(a * b) // gcd(a, b) if a and b else 0
    return reduce(lcm, [nums[894], nums[801]])