def find_primes_between_indices(lst):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(lst) < 950:
        return []
    primes = [x for x in lst[478:950] if is_prime(x)]
    return sorted(primes, reverse=True)