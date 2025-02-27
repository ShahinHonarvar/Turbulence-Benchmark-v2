def prime_factors(numbers_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    sixth_number = numbers_list[6]
    prime_factors_set = set()
    for i in range(2, sixth_number + 1):
        while sixth_number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            sixth_number //= i
        if sixth_number == 1:
            break
    return prime_factors_set