def find_primes_between_indices(a_list):

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [i for i in a_list[11:42] if is_prime(i)]
    return sorted(primes, reverse=True)