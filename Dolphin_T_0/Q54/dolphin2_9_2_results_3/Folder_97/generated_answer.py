def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = input_tuple[645]
    numbers = [i for i in range(2, x) if is_prime(i)]
    right_truncatables = []
    for num in numbers:
        trunc = num
        while trunc > 0:
            if is_prime(trunc):
                right_truncatables.append(trunc)
                trunc //= 10
            else:
                break
    return sorted(list(set(right_truncatables)))