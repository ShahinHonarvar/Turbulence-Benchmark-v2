def all_left_truncatable_prime(numbers):
    x = numbers[645]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return n in [2, 3, 5, 7]
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) + 1):
            if int(s[i - 1:]) not in prime_list:
                return False
        return True
    prime_list = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    result = []
    for num in prime_list:
        if is_left_truncatable_prime(num):
            result.append(num)
    return result