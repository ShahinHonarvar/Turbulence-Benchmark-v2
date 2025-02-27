def all_left_right_truncatable_prime(n):

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
    if n[69] < 2:
        return []
    primes = [i for i in range(2, n[69] + 1) if is_prime(i)]
    lrt_primes = []
    for prime in primes:
        lrt_flag = True
        for digit in str(prime):
            if digit == '0':
                lrt_flag = False
                break
        for i in range(len(str(prime)) - 1):
            if not is_prime(int(str(prime)[1:] + str(prime)[-1])):
                lrt_flag = False
                break
        if lrt_flag:
            lrt_primes.append(prime)
    return sorted(lrt_primes, reverse=True)