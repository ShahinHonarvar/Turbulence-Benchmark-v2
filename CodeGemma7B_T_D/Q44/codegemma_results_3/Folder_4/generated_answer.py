from math import sqrt as sq

def composite_nums_between_indices(list_of_nums):
    """
    This function takes a list of positive integers and returns the set of all composite numbers
    in the given list that are between index 56 to index 98, both inclusive. If no composite number exists in the
    specified range, the function should return an empty set.

    Args:
      list_of_nums: A list of positive integers.

    Returns:
      A set of composite numbers in the given list between index 56 to index 98, both inclusive.
    """
    composite_numbers = set()
    for i in range(56, 99):
        if is_composite(list_of_nums[i]):
            composite_numbers.add(list_of_nums[i])
    return composite_numbers

def is_composite(num):
    """
    This function checks if a number is composite. A number is composite if it has
    more than two factors, including 1 and itself.

    Args:
      num: The number to check.

    Returns:
      True if the number is composite, False otherwise.
    """
    if num == 1:
        return False
    if num % 2 == 0:
        return True
    for i in range(3, int(sq(num)) + 1, 2):
        if num % i == 0:
            return True
    return False