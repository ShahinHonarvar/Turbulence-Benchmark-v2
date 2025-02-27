def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[81]
    prime_nums = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                prime_nums.append(num)
    return sorted(prime_nums, reverse=True)