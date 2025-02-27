import math

def all_right_truncatable_prime(t: tuple) -> list:
    x = t[52]
    is_prime = lambda num: all((num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)))
    right_trunc_prime = []
    for i in range(2, x):
        if is_prime(i):
            right = i
            while right > 0:
                if not is_prime(right):
                    break
                right //= 10
            else:
                right_trunc_prime.append(i)
    right_trunc_prime.sort(reverse=True)
    return right_trunc_prime