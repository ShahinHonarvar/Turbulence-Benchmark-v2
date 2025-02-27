def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_618 = numbers_list[617]
    num_195 = numbers_list[194]
    return gcd(num_618, num_195)