def composite_nums_between_indices(nums):
    """
    Given a list of positive integers, return the set of all composite numbers
    in the given list that are between index 0 to index 9, both inclusive. If
    no composite number exists in the specified range, return an empty set.
    """
    composites = set()
    for i in range(10):
        if nums[i] > 1 and (not (nums[i] == 2 or nums[i] == 3)):
            if is_composite(nums[i]):
                composites.add(nums[i])
    if not composites:
        return set()
    return composites

def is_composite(num):
    """
    Determines if a given number is composite. A number is composite if it is
    divisible by a number other than 1 and itself.
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False