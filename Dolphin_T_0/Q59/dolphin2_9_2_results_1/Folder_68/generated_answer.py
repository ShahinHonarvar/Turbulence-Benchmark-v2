def all_left_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_integers[1]
    prime_numbers_list = []
    for i in range(x, 1, -1):
        if is_prime(i):
            if i % 10 == 0 or i == 1:
                continue
            else:
                result = i
                while result >= 10:
                    if not is_prime(result):
                        break
                    result //= 10
                if result < 10:
                    prime_numbers_list.append(i)
    prime_numbers_list.sort(reverse=True)
    return prime_numbers_list