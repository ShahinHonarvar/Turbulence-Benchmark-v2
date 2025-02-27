def gcf_two_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num_list[198], num_list[212])