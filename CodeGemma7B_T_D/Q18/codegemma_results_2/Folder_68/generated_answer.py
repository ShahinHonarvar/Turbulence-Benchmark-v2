def sum_ints_div_by_either_nums(nums: list[int]) -> int:
    """
            Sums integers divisible by either 5 or 7 from index 7 to 7, inclusive.

            Args:
            nums: A list of integers.

            Returns:
            The sum of integers divisible by either 5 or 7 from index 7 to index 7, inclusive. If no such integers exist, the function should return 0.
            """
    start_idx = min((i for i in range(7, len(nums)) if nums[i] % 5 == 0 or nums[i] % 7 == 0), default=None)
    if start_idx is None:
        return 0
    end_idx = max((i for i in range(7, len(nums)) if nums[i] % 5 == 0 or nums[i] % 7 == 0), default=None)
    sum_nums = sum(nums[start_idx:end_idx + 1])
    return sum_nums