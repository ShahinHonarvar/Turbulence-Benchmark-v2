def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_set = set()
    num = numbers_list[1]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_set.add(i)
            num //= i
        if num == 1:
            break
    return prime_set