def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_indices = [idx for idx, num in enumerate(lst) if is_prime(num)]
    if prime_indices[459] > prime_indices[781]:
        return []
    start, end = (prime_indices[459], prime_indices[781])
    return sorted(lst[start:end + 1]) if start != end else lst[end]