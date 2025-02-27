def all_left_truncatable_prime(n):

    def is_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
    x = n[803]
    result = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(result)