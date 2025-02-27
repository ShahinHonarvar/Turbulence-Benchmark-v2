from itertools import count

def all_right_truncatable_prime(t):
    x = t[433]

    def generate_prime():
        prime = [True] * (x + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(x ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, x + 1, i):
                    prime[j] = False
        return prime

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes():
        prime = generate_prime()
        right_truncatable_primes = []
        for i in range(2, x):
            if prime[i]:
                num = i
                while num > 0:
                    if not prime[num % 10]:
                        break
                    num //= 10
                else:
                    right_truncatable_primes.append(i)
        return right_truncatable_primes
    return sorted(generate_right_truncatable_primes(), reverse=True)