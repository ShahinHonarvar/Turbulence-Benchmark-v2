def all_left_truncatable_prime(x):
    prime = [n for n in range(2, x) if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1)))]

    def left_truncatable(n):
        for sub in range(1, len(str(n))):
            if int(str(n)[:sub]) % 2 == 0 or int(str(n)[:sub]) % 3 == 0:
                return False
            prime_flag = True
            for p in prime:
                if p > int(str(n)[:sub]):
                    break
                if int(str(n)[:sub]) % p == 0:
                    prime_flag = False
                    break
            if prime_flag == False:
                return False
        return True
    return sorted([p for p in prime if left_truncatable(p)], reverse=True)