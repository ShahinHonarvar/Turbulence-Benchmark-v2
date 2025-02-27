def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_634 = numbers_list[634]
    num_585 = numbers_list[585]
    gcf = gcd(num_634, num_585)
    return gcf