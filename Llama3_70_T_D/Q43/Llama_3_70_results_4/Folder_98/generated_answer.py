def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) < 3:
        return []
    index1 = numbers[0]
    index2 = numbers[1]
    if index1 > index2:
        index1, index2 = (index2, index1)
    if index1 < 0 or index2 >= len(numbers) - 2:
        return []
    primes = [numbers[i] for i in range(index1 + 2, index2 + 3) if is_prime(numbers[i])]
    return sorted(primes, reverse=True)