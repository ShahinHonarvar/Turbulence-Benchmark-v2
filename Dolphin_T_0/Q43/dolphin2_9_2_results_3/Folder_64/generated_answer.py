def find_primes_between_indices(int_list):

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            else:
                return True
        else:
            return False
    potential_primes = int_list[7:10]
    primes = [num for num in potential_primes if is_prime(num)]
    return sorted(primes, reverse=True) if primes else []