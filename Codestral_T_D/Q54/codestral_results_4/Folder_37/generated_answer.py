def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def truncate_right(n):
        return int(str(n)[:-1])
    x = numbers[35]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num = truncate_right(num)
            if num == 0:
                result.append(i)
    return sorted(result, reverse=True)