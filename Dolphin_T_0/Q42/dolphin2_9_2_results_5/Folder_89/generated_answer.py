def prime_factors(lst):
    """
    Function to find prime factors of the 19th number in the list
    """

    def is_prime(num):
        if num == 2:
            return True
        if num % 2 == 0 or num == 1:
            return False
        return all((num % i for i in range(3, int(num ** 0.5) + 1, 2)))
    num = lst[18]
    prime_factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors