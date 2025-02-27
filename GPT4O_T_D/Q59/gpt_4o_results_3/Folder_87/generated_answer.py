def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable_prime(n):
        n_str = str(n)
        return '0' not in n_str and all((is_prime(int(n_str[i:])) for i in range(len(n_str))))
    x = numbers[39]
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)], reverse=True)