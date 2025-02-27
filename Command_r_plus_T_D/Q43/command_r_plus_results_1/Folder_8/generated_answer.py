def find_primes_between_indices(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index = 43
    end_index = 76
    primes = []
    for index in range(start_index, end_index + 1):
        if is_prime(numbers_list[index]):
            primes.append(numbers_list[index])
    return sorted(primes, reverse=True)