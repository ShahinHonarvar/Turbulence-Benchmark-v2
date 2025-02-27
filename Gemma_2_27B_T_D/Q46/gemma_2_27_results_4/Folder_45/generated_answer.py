def gcf_three_nums(nums):
    a = nums[46]
    b = nums[84]
    c = nums[23]
    while True:
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        if b < c:
            b, c = (c, b)
        if a == b == c:
            return a
        if a == b:
            return gcd(a, c)
        if a == c:
            return gcd(a, b)
        return gcd(b, c)

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a