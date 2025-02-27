def all_left_truncatable_prime(n):

    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        sqrt_num = int(num ** 0.5) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False
        return True
    n = n[28]
    left_truncatable_primes = []
    for i in range(2, n):
        if is_prime(i):
            temp = i
            while temp != 0:
                if is_prime(temp):
                    temp = temp // 10
                else:
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)