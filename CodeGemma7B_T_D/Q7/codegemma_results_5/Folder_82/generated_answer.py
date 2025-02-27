def all_even_ints_inclusive(nums: list) -> list:
    even_nums = [num for num in nums[20:201] if num % 2 == 0]
    return even_nums if even_nums else []