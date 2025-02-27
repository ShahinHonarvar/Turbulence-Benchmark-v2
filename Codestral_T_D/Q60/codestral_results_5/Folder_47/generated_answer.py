def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[49]
    primes = [2]
    for possiblePrime in range(3, x + 1, 2):
        if all((possiblePrime % prime != 0 for prime in primes)):
            primes.append(possiblePrime)

    def is_truncatable_prime(num):
        if num < 2:
            return False
        str_num = str(num)
        if '0' in str_num:
            return False
        return all((int(str_num[i:]) in primes and int(str_num[:i]) in primes for i in range(1, len(str_num))))
    return sorted((num for num in primes if is_truncatable_prime(num)))