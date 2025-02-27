def all_right_truncatable_prime(n):
    """
  Returns the list of all right-truncatable prime numbers less than x.
  """
    x = n[784]
    primes = [x]
    for i in range(2, x):
        if x % i == 0:
            continue
        for j in range(1, len(str(i))):
            if int(str(i)[:-j]) == 0:
                continue
            if not is_prime(int(str(i)[:-j])):
                break
        else:
            primes.append(i)
    return sorted(primes)

def is_prime(x):
    """
  Checks if a number is prime.
  """
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True