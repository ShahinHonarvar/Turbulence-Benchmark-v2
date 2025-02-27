def all_left_truncatable_prime(a_tuple):

    def is_left_truncatable_prime(num):
        num = str(num)
        for i in range(len(num)):
            if num[i] == '0' or not sympy.isprime(int(num[i:])):
                return False
        return True

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = a_tuple[4]
    all_left_truncatable_prime_numbers = []
    for num in range(2, x):
        if is_left_truncatable_prime(num) and is_prime(num):
            all_left_truncatable_prime_numbers.append(num)
    return sorted(all_left_truncatable_prime_numbers)