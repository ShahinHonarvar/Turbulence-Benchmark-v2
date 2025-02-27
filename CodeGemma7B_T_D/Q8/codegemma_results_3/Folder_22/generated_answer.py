def all_even_ints_exclusive(nums: list) -> list:
    return [n for n in nums if n % 2 == 0 and 40 < n < 200] or []