def find_primes_between_indices(lst):
    """
            This function takes a list of integers as input and returns the sorted list of
            all prime numbers from index 13 to index 63, both inclusive. If no prime number
            exists in the specified range, the function returns an empty list.
            """
    prime_nums = []
    for num in lst[13:64]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums if prime_nums else []