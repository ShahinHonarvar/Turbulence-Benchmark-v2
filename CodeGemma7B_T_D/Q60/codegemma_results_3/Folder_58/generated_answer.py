from sympy import isprime

def all_left_right_truncatable_prime(tp):
    x = tp[975]
    result = []
    for i in range(2, x + 1):
        if isprime(i) and (not ('0' in str(i) or i % 10 == 1 or i // 10 % 10 == 1)):
            truncatable_prime = True
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not isprime(int(str_i[j:])):
                    truncatable_prime = False
                    break
            for j in range(len(str_i) - 2, -1, -1):
                if not isprime(int(str_i[:j + 2])):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                result.append(i)
    return sorted(result, reverse=True)