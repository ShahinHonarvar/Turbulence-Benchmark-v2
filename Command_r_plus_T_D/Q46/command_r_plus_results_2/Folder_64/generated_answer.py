def gcf_three_nums(nums_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    first_num = nums_list[0]
    eighth_num = nums_list[8]
    third_num = nums_list[3]
    gcf = gcd(gcd(first_num, eighth_num), third_num)
    return gcf