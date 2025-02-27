def all_left_truncatable_prime(t):
    """
  Write a function called 'all_left_truncatable_prime' that takes an argument which is a tuple of positive integers.
  Let x be the integer at index 758. The function should return the list of all left-truncatable prime numbers less than x.
  The return list should be sorted in ascending order.
  A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
  """
    x = t[758]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            number = str(n)
            for i in range(1, len(number)):
                if is_prime(int(number[i:])):
                    left_truncatable_primes.append(n)
                    break
    left_truncatable_primes.sort()
    return left_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True