def sum_even_ints_inclusive(nums):
    """
            Sums all even numbers from 25th to 59th indices inclusive in the list.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all even numbers from 25th to 59th indices inclusive. Otherwise, 0.
            """
    total = 0
    if len(nums) < 59:
        return 0
    for i in range(25, 60):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total