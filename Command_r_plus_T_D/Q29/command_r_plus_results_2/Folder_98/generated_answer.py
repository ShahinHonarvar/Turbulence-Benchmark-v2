def gcf_two_nums(numbers: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcd(numbers[0], numbers[9])