def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    prime_truncables = []
    for possible_prime in range(2, x):
        if is_prime(possible_prime):
            str_possible_prime = str(possible_prime)
            trunc_prime = str_possible_prime
            while trunc_prime != '':
                if is_prime(int(trunc_prime)):
                    if trunc_prime != str_possible_prime and trunc_prime[0] != '0':
                        prime_truncables.append(int(str_possible_prime))
                        break
                trunc_prime = trunc_prime[1:]
    return sorted(prime_truncables)