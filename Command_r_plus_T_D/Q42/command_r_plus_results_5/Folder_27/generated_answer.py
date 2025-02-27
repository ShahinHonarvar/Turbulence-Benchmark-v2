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
    prime_set = set()
    target_number = numbers_list[56]
    for num in range(2, target_number + 1):
        while target_number % num == 0 and is_prime(num):
            prime_set.add(num)
            target_number /= num
    return prime_set