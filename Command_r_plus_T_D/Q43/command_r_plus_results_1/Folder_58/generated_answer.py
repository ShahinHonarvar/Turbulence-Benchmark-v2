def find_primes_between_indices(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index = 157
    end_index = 735
    primes = []
    for index in range(start_index, end_index + 1):
        num = numbers_list[index]
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)