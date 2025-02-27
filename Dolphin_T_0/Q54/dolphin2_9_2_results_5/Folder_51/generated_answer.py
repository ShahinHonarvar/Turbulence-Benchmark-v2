def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[54]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                if is_prime(truncated_num):
                    truncated_num //= 10
                else:
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True