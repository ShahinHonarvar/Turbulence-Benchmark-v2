def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_51 = numbers_list[51]
    num_27 = numbers_list[27]
    gcf = gcd(num_51, num_27)
    return gcf