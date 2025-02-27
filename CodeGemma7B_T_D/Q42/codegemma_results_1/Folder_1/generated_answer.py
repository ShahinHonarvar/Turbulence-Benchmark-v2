def prime_factors(lst):
    prime_factors = set()

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_factors_helper(num):
        if num == 1:
            return
        if is_prime(num) and num not in prime_factors:
            prime_factors.add(num)
            return
        for divisor in range(2, num + 1):
            if is_prime(divisor) and num % divisor == 0:
                prime_factors.add(divisor)
                prime_factors_helper(num // divisor)
                break
    prime_factors_helper(lst[85])
    return prime_factors