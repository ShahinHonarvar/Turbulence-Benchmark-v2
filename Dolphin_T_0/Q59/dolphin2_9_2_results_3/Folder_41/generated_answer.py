def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        if num < 2 or not str(num).count('0'):
            return False
        for c in str(num):
            if not is_prime(int(c)):
                return False
        return True

    def left_truncatable_primes(n):
        return [i for i in range(2, n) if is_left_truncatable(i)]

    def descending(lst):
        return sorted(lst, reverse=True)
    x = numbers[46]
    return descending(left_truncatable_primes(x))