import typing

def all_even_ints_exclusive(nums: typing.List[int]) -> typing.List[int]:
    return [num for num in nums[743:867] if num % 2 == 0]