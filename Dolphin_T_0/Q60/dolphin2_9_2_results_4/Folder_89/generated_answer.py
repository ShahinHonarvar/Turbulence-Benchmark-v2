def isPrime(n):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return False

def all_left_right_truncatable_prime(t):
    x = t[97]
    prime_list = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if not '0' in str_i:
            truncatable = True
            for j in range(len(str_i) - 2):
                trunc_str_i = str_i[j + 1:-(j + 1)]
                if not isPrime(int(trunc_str_i)):
                    truncatable = False
                    break
            if truncatable and isPrime(i):
                prime_list.append(i)
    return sorted(prime_list, reverse=True) if prime_list else []