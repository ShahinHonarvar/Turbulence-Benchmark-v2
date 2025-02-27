def all_left_truncatable_prime(args):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    def generate_left_truncatable_primes(n):
        result = []
        for i in range(11, n):
            if '0' not in str(i) and is_prime(i) and left_truncatable(i):
                result.append(i)
        return result
    return sorted(generate_left_truncatable_primes(args[61]))