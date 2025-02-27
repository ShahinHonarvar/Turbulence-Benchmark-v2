def find_primes_between_indices(lst):
    if len(lst) < 63:
        return []

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
    selected_numbers = lst[25:63]
    primes = [num for num in selected_numbers if is_prime(num)]
    return sorted(primes)