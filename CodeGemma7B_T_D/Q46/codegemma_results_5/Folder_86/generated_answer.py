def gcf_three_nums(nums):
    a, b, c = (nums[341], nums[238], nums[374])
    gcd = a
    while gcd > 0 and gcd % b != 0 and (gcd % c != 0):
        gcd -= 1
    return gcd