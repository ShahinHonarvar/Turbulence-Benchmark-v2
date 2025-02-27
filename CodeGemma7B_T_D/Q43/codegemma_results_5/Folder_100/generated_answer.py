def find_primes_between_indices(nums):
    """
            This function takes a list of integers and returns a sorted list of all prime numbers from index 25 to index 62, both inclusive. The returned list should be in ascending order. If no prime number exists in the specified range, the function should return an empty list.
            """
    Primes = []
    for i in range(25, 63):
        b = True
        for j in range(2, i):
            if i % j == 0:
                b = False
                break
        if b == True:
            Primes.append(i)
    return sorted(Primes)