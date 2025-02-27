def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(numbers_list[41], numbers_list[69])