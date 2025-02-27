from sympy import isprime

def all_left_truncatable_prime(num):
    prime_list = [i for i in num if isprime(i)]
    result_list = set()
    for i in prime_list:
        str_i = str(i)
        if '0' not in str_i:
            if all((isprime(int(str_i[j:])) for j in range(1, len(str_i)))):
                result_list.add(i)
    return sorted(result_list)