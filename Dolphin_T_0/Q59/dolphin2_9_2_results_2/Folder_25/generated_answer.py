def all_left_truncatable_prime(num):

    def is_truncatable(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i ** 2 <= n:
            if n % i == 0 or all_left_truncatable_prime(int(str(n)[1:])) == False:
                return False
            i += 2
        return True
    x = num[92]
    trunc_primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        if all_left_truncatable_prime(i):
            trunc_primes.append(i)
    return sorted(list(set(trunc_primes)))