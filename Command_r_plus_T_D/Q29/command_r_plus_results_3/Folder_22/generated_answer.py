def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(numbers_list[24], numbers_list[68])