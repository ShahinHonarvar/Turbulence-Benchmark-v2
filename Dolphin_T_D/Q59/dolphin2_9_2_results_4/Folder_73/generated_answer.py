def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[97]
    primes = []
    for i in range(2, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        if not is_prime(i):
            continue
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])):
                break
            if j + 1 == len(str_i):
                primes.append(i)
    return sorted(primes)