def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_47 = numbers_list[47]
    num_10 = numbers_list[10]
    gcf = gcd(num_47, num_10)
    return gcf