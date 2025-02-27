def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        not_prime = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                not_prime.append(i)
        if not_prime:
            return False
        else:
            return True

    def is_truncatable_prime(n):
        if not all([int(i) != 0 for i in str(n)]):
            return False
        length = len(str(n))
        for x in range(length - 1):
            if not is_prime(int(str(n)[x:length])):
                return False
            if not is_prime(int(str(n)[1:length - x])):
                return False
        return True
    x = numbers_tuple[11]
    result = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(result)