def all_even_ints_exclusive(list):
    nums = list[276:376]
    return [n for n in nums if n % 2 == 0] or []