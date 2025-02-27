def find_primes_between_indices(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index = 35
    end_index = 89
    primes = []
    for i in range(start_index, end_index + 1):
        if is_prime(numbers_list[i]):
            primes.append(numbers_list[i])
    primes.sort(reverse=True)
    return primes