def find_primes_between_indices(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for num in numbers_list[33:36]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)