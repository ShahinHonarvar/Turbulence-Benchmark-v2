def all_left_truncatable_prime(num):
    if num[81] >= 2 and num[81] <= 9:
        lcp = []
        for i in range(2, num[81]):
            if all_left_truncatable_prime.is_prime(i) and (not all_left_truncatable_prime.has_zero(i)):
                prime_str = str(i)
                for j in range(1, len(prime_str)):
                    if not all_left_truncatable_prime.is_prime(int(prime_str[j:])):
                        break
                else:
                    lcp.append(i)
        lcp.sort()
        lcp.reverse()
        return lcp
    else:
        return []

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def has_zero(num):
    str_num = str(num)
    return str_num.count('0') > 0