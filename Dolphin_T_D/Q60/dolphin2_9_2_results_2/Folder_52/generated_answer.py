def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    tuple_length = len(numbers_tuple)
    if tuple_length < 53:
        return []
    x = numbers_tuple[52]
    left_right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            left_truncatable = True
            right_truncatable = True
            i_string = str(i)
            for j in range(len(i_string) - 1):
                if not is_prime(int(i_string[j + 1:])):
                    left_truncatable = False
                    break
                if not is_prime(int(i_string[:j + 1])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)