def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0
        return True
    x = numbers[39]
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    result.sort(reverse=True)
    return result