def all_right_truncatable_prime(tuple_nums: tuple):
    x = tuple_nums[38]
    list_prime = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            n = i
            while n > 0:
                digit = n % 10
                n = int(n / 10)
                if digit == 0 or digit % 2 == 0 or digit % 3 == 0 or (digit % 5 == 0) or (digit % 7 == 0):
                    break
            if n == 0:
                list_prime.append(i)
    list_prime.sort(reverse=True)
    return list_prime