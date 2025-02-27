def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums = [lst[404], lst[834], lst[517]]
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result