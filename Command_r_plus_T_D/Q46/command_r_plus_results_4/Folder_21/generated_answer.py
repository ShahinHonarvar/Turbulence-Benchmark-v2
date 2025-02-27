def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_412 = numbers_list[411]
    num_932 = numbers_list[931]
    num_337 = numbers_list[336]
    gcf = gcd(num_412, num_932)
    gcf = gcd(gcf, num_337)
    return gcf