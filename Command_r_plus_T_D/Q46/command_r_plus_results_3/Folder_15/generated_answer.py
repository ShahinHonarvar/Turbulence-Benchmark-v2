def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_1 = numbers[4]
    num_2 = numbers[0]
    num_3 = numbers[8]
    gcf = gcd(num_1, num_2)
    gcf = gcd(gcf, num_3)
    return gcf