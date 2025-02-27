def prime_factors(num_list):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    num = num_list[13]
    result = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            result.add(i)
    return result