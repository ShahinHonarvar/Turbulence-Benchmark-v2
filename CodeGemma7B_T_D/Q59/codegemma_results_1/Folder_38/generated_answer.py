from math import isprime

def all_left_truncatable_prime(x):
    left_truncatable_prime = []
    for number in range(2, x):
        number_str = str(number)
        if '0' not in number_str and isprime(number):
            for i in range(1, len(number_str)):
                if not isprime(int(number_str[i:])):
                    break
            else:
                left_truncatable_prime.append(number)
    return sorted(left_truncatable_prime)