def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    prime_list = [n for n in lst[31:93] if is_prime(n)]
    prime_list.sort(reverse=True)
    return prime_list