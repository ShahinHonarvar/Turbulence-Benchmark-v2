def all_left_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_integers[77]
    result = []
    for num in range(2, x):
        left_truncatable = True
        number = num
        while number != 0:
            if not is_prime(number):
                left_truncatable = False
                break
            number //= 10
        if left_truncatable:
            result.append(num)
    return sorted(result)