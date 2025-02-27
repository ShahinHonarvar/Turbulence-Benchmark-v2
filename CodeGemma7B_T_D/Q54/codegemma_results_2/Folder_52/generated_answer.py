from math import sqrt

def all_right_truncatable_prime(given_tuple):
    """
    Your answer here
    """
    x = given_tuple[52]
    prime_list = [i for i in range(2, x + 1)]
    for i in range(2, int(sqrt(x)) + 1):
        if i in prime_list:
            for j in range(i * i, x + 1, i):
                prime_list.remove(j)
    right_truncatable_primes = []
    for num in prime_list:
        str_num = str(num)
        for d in range(1, len(str_num)):
            truncatable_num = int(str_num[:-d])
            if truncatable_num in prime_list:
                right_truncatable_primes.append(num)
                break
            if truncatable_num not in prime_list:
                break
    return sorted(right_truncatable_primes, reverse=True)