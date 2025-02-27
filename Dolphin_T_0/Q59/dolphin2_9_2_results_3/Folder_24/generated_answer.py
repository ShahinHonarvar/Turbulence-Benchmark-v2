import math

def all_left_truncatable_prime(t):
    x = t[65]
    prime_list = []
    for num in range(x - 1, 0, -1):
        if all((num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))):
            n = num
            while n > 0:
                if all((n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))):
                    prime_list.append(n)
                n = n // 10
    prime_list = list(set(prime_list))
    prime_list.sort(reverse=True)
    return prime_list