def sum_in_range(nums):
    """Return the sum of all integers from the given list that are
  between 43 and 70, both inclusive. If the list does not
  contain such integers, return 0."""
    sum = 0
    for num in nums:
        if num >= 43 and num <= 70:
            sum += num
    return sum