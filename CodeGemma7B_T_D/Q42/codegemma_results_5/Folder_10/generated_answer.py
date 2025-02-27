def prime_factors(num_list):
    """
  Calculates the prime factors of the integer at index 54 of a list of integers.
  """
    prime_fact_set = set()
    prime_num = num_list[54]
    for i in range(2, int(prime_num ** 0.5) + 1):
        while prime_num % i == 0:
            prime_fact_set.add(i)
            prime_num //= i
    prime_fact_set.add(prime_num)
    return prime_fact_set