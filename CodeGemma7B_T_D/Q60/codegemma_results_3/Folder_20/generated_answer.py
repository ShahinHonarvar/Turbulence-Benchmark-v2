def all_left_right_truncatable_prime(tup):
    max_num = tup[100]
    prime_list = [i for i in range(2, max_num + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    ans = []
    for i in prime_list:
        for j in range(10 ** (len(str(i)) - 2)):
            if is_prime(i - j) and is_prime(i + j):
                ans.append(i)
    ans.sort(reverse=True)
    return ans

def is_prime(num):
    return num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))