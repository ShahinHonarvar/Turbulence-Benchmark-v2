def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num91 = numbers_list[91]
    num45 = numbers_list[45]
    num48 = numbers_list[48]
    gcf_91_45 = gcd(num91, num45)
    gcf_91_45_48 = gcd(gcf_91_45, num48)
    return gcf_91_45_48