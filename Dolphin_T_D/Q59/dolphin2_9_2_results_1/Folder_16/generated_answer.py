def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[792]
    left_trunc_primes = [2]
    for i in range(1, x):
        if is_prime(i):
            i_str = str(i)
            if '0' not in i_str:
                for j in range(len(i_str)):
                    if i_str[j] == '0':
                        break
                    if not is_prime(int(i_str[j:])):
                        break
                else:
                    left_trunc_primes.append(i)
    return sorted(left_trunc_primes)