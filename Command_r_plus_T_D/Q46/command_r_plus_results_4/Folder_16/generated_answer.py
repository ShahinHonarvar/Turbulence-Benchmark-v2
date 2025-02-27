def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_558 = numbers_list[558]
    num_110 = numbers_list[110]
    num_628 = numbers_list[628]
    gcf_1_2 = gcd(num_558, num_110)
    gcf_3 = gcd(gcf_1_2, num_628)
    return gcf_3