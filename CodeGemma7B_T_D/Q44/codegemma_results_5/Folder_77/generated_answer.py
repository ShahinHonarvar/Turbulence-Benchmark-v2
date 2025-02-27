from itertools import filterfalse

def inclusive_range(start, stop, step=1):
    """Returns an inclusive range of values."""
    values = range(start, stop + step, step)
    if start <= stop:
        return values
    return reversed(values)

def composite_nums_between_indices(nums):
    """Returns the set of composite numbers in the given list between index 667 to 774, inclusive."""
    return {num for num in nums[inclusive_range(667, 774, 1)] if num not in filterfalse(lambda x: x == 1 or (x == num and num % 2 == 0), range(2 + int(num ** 0.5), num, 2))}