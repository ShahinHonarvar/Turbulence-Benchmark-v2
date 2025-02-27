def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index1 = lst[0]
    index2 = lst[1]
    numbers = lst[index1:index2 + 1]
    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes, reverse=True)