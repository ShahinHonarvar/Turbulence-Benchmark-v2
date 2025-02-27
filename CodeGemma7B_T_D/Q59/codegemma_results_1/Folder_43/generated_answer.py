def all_left_truncatable_prime(x):
    answer = set()

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) % 2 == 0 or int(str_n[i:]) % 3 == 0:
                return False
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for num in x:
        if is_prime(num) and is_left_truncatable_prime(num):
            answer.add(num)
    return sorted(answer, reverse=True)