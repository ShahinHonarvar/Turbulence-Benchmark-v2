def composite_nums_between_indices(int_list):
    """
  Write a function called 'composite_nums_between_indices' that takes one argument, a list of positive integers. The function should return the set of all composite numbers in the given list that are between index 50 to index 54, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
  """
    composite_nums = set()
    for idx, num in enumerate(int_list):
        if 50 <= idx <= 54 and (not is_prime(num)):
            composite_nums.add(num)
    return composite_nums

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True