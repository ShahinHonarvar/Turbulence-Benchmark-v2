def find_primes_between_indices(lst: list) -> list:
    """
            This function takes one argument, a list of integers, and returns
            the sorted list of all prime numbers from index 3 to index 8, both inclusive.
            The returned list should be in ascending order. If no prime number exists in the
            specified range, the function should return an empty list.
            """
    prime_list = []
    for i in range(3, 8 + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    prime_list.sort()
    return prime_list