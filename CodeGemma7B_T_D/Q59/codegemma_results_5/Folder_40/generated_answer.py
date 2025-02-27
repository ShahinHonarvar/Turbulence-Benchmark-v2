def all_left_truncatable_prime(x):
    """
  Write a function called 'all_left_truncatable_prime' that takes an argument which is a tuple of positive integers. Let x be the integer at index 10. The function should return the list of all left-truncatable prime numbers less than x. The return list should be sorted in descending order. A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
  """
    result = []
    for candidate in list(range(2, x)):
        if is_prime(candidate) and (not has_zero(candidate)) and is_left_truncatable_prime(candidate):
            result.append(candidate)
    return sorted(result, reverse=True)

def is_prime(candidate):
    for divisor in range(2, int(candidate ** 0.5) + 1):
        if candidate % divisor == 0:
            return False
    return True

def has_zero(candidate):
    return True if '0' in str(candidate) else False

def is_left_truncatable_prime(candidate):
    candidate_str = str(candidate)
    for i in range(1, len(candidate_str)):
        if not is_prime(int(candidate_str[i:])):
            return False
    return True