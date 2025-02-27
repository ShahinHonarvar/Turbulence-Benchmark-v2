def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num90 = numbers_list[90]
    num54 = numbers_list[54]
    num96 = numbers_list[96]
    gcf_90_54 = gcd(num90, num54)
    gcf_90_54_96 = gcd(gcf_90_54, num96)
    return gcf_90_54_96