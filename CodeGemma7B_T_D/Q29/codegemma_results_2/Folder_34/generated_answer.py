def gcf_two_nums(nums):
    return gcd(nums[60], nums[64])

def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

def main():
    nums = [12, 8, 20, 36, 45, 72, 60, 24, 50, 90]
    gcf = gcf_two_nums(nums)
    print(gcf)