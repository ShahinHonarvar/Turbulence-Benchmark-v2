def is_left_and_right_truncatable_prime(n, primes_set):
    num_str = str(n)
    length = len(num_str)
    for i in range(length):
        for j in range(length - i):
            if num_str[j] == '0' and j != length - 1 or not num_str[j:length - i + j].isdigit() or (not n % int(num_str[j:length - i + j])) or (not int(num_str[j:length - i + j]) in primes_set):
                return False
    return True

def all_left_right_truncatable_prime(n):
    left_right_trunc_primes = []
    primes_set = set()
    for num in range(2, n + 1):
        if num in primes_set:
            if is_left_and_right_truncatable_prime(num, primes_set):
                left_right_trunc_primes.append(num)
        elif is_left_and_right_truncatable_prime(num, primes_set):
            left_right_trunc_primes.append(num)
            primes_set.add(num)
    return left_right_trunc_primes