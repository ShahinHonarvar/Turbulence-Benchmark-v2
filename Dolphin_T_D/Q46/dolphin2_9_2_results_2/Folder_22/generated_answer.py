def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(three_nums):
    index_27 = three_nums[27]
    index_85 = three_nums[85]
    index_51 = three_nums[51]
    return gcd(gcd(index_27, index_85), index_51)