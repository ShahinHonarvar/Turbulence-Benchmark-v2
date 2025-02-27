def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_69 = numbers_list[69]
    num_41 = numbers_list[41]
    return gcd(num_69, num_41)