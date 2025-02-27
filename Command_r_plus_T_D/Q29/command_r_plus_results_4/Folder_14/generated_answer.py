def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_49 = numbers_list[49]
    num_53 = numbers_list[53]
    return gcd(num_49, num_53)