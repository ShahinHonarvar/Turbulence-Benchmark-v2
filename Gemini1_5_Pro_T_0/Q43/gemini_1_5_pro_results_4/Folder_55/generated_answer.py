def find_primes_between_indices(input_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    if len(input_list) > 9:
        for num in input_list[9:10]:
            if is_prime(num):
                primes.append(num)
    primes.sort()
    return primes