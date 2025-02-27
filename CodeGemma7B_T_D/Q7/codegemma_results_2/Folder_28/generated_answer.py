def all_even_ints_inclusive(nums: list[int]) -> list[int]:
    if not any((n % 2 == 0 for n in nums[62:64])):
        return []
    return [n for n in nums[62:64] if n % 2 == 0]