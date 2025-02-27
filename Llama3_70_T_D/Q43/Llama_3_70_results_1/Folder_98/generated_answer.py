def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    try:
        start = lst.index(1)
        end = lst.index(2)
    except ValueError:
        return []
    return sorted([num for num in lst[min(start, end):max(start, end) + 1] if is_prime(num)], reverse=True)