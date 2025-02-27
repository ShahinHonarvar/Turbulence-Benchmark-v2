def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_56 = numbers_list[56]
    num_54 = numbers_list[54]
    num_13 = numbers_list[13]
    gcf = gcd(num_56, num_54)
    gcf = gcd(gcf, num_13)
    return gcf