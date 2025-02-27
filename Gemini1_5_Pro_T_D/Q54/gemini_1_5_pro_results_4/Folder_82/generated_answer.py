def all_right_truncatable_prime(numbers):
    x = numbers[69]

    def is_right_truncatable_prime(num):
        if num <= 1:
            return False
        if num in {2, 3, 5, 7}:
            return True
        if num % 2 == 0 or num % 5 == 0:
            return False
        str_num = str(num)
        for i in range(len(str_num) - 1, 0, -1):
            if int(str_num[:i]) not in primes:
                return False
        return True
    primes = set()
    for num in range(2, x):
        if all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    result = sorted(filter(is_right_truncatable_prime, range(2, x)), reverse=True)
    return result