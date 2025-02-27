from sympy import isprime

def all_left_truncatable_prime(x):
    """
  x = tuple of positive integers
  return list of left truncation prime number in descending order
  """
    ans = []
    for i in range(x[54] - 1, 1, -1):
        if isprime(i) and all((isprime(int(str(i)[:j])) for j in range(len(str(i)) - 1))):
            ans.append(i)
    return sorted(ans, reverse=True)