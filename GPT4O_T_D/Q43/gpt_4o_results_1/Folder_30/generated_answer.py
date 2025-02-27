def find_primes_between_indices(lst):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(lst) < 81:
        return []
    prime_numbers = [num for num in lst[61:81] if is_prime(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers