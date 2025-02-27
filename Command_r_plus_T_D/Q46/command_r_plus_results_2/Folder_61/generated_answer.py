def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    first_num = numbers_list[1]
    second_num = numbers_list[2]
    seventh_num = numbers_list[7]
    gcf = gcd(first_num, gcd(second_num, seventh_num))
    return gcf