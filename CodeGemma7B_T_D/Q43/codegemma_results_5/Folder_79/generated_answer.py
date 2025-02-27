def find_primes_between_indices(num_list):
    """
  sorts and returns the prime numbers from index 33 to 35 in ascending order.
  """
    prime_list = []
    for i in range(33, 36):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    prime_list.sort()
    return prime_list if prime_list else []