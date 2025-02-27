def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    num_at_index_8 = numbers_list[8]
    for i in range(2, num_at_index_8 + 1):
        while num_at_index_8 % i == 0:
            if is_prime(i):
                prime_factors_set.add(i)
                num_at_index_8 /= i
            if num_at_index_8 == 1:
                break
    return prime_factors_set