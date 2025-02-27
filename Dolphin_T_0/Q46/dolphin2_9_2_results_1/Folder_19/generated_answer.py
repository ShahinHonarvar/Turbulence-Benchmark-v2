def gcf_three_nums(nums_list):

    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(nums_list[40], gcd(nums_list[15], nums_list[99]))