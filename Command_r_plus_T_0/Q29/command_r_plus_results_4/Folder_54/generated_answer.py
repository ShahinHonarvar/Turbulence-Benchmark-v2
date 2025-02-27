def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_56 = numbers_list[56]
    num_92 = numbers_list[92]
    gcf = gcd(num_56, num_92)
    return gcf