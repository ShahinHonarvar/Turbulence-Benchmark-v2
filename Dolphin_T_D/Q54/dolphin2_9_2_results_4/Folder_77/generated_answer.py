def all_right_truncatable_prime(tuple_in):
    x = tuple_in[767]

    def check_prime(n):
        if n == 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable(n):
        list_n = [int(i) for i in str(n)]
        while len(list_n) != 0:
            if check_prime(int(''.join(map(str, list_n)))) == False:
                return False
            else:
                list_n.pop()
        return True
    list_primes = [i for i in range(2, x) if check_prime(i) and is_right_truncatable(i)]
    list_primes.sort(reverse=True)
    return list_primes