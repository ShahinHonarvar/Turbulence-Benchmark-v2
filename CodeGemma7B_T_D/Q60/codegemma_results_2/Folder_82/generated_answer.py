def all_left_right_truncatable_prime(num):
    """
  num is a tuple containing the upper limit to search for left-right truncatable prime numbers.
  """
    prime_list = [i for i in range(2, num[69] + 1) if all((j > 1 and i % j for j in range(2, int(i ** 0.5) + 1)))]
    return sorted([n for n in prime_list if is_left_right_truncatable(n)], reverse=True)

def is_left_right_truncatable(n):
    """
  n is a positive integer.
  """
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        left = int(n_str[i:])
        right = int(n_str[:-i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def is_prime(n):
    """
  n is a positive integer.
  """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True