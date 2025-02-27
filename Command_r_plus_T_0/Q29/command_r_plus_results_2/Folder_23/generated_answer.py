def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_48 = numbers_list[48]
    num_74 = numbers_list[74]
    gcf = gcd(num_48, num_74)
    return gcf