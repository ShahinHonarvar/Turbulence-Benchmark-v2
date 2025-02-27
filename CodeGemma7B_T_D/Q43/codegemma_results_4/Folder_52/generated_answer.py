def find_primes_between_indices(number_list):
    """
    Finds and returns the sorted list of prime numbers between index 33 to index 59, both inclusive.

    Args:
        number_list: A list of integers.

    Returns:
        A sorted list of prime numbers from index 33 to index 59, both inclusive. If no prime number exists in the specified range, returns an empty list.
    """
    primes = []
    for number in number_list[33:60]:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    primes.sort(reverse=True)
    return primes