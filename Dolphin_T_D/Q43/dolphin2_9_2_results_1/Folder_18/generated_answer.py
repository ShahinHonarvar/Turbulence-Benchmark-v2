def find_primes_between_indices(lst):

    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return sorted([x for x in lst[430:806] if check_prime(x)])