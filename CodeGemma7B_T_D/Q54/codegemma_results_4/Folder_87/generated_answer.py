def all_right_truncatable_prime(x):
    """
  A function called all_right_truncatable_prime that takes an argument which is a tuple of positive integers.
  Let x be the integer at index 39.
  The function should return the sorted list of all right-truncatable prime numbers less than x.
  The returned list should be sorted in descending order.
  If there is no such right-truncatable prime number, the function should return an empty list.
  A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
  """
    all_tuples = []
    for i in range(2, x):
        n = i
        prime_chain = []
        while n > 1:
            if is_prime(n):
                prime_chain.append(n)
                n //= 10
            else:
                break
        is_right_truncatable = True
        for val in prime_chain:
            if not is_prime(val):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            all_tuples.append((prime_chain[0], prime_chain))
    return sorted(all_tuples, reverse=True) if all_tuples else []

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True