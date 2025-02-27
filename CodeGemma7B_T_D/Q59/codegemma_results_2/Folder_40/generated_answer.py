from sympy import isprime

def all_left_truncatable_prime(args):
    tuple = list(args)
    x = tuple[10]
    list_of_prime = []
    for a in range(2, x):
        str_a = str(a)
        for b in range(len(str_a)):
            sub = str_a[b:]
            if isprime(int(sub)) and sub != '0':
                list_of_prime.append(a)
                break
    return sorted(list_of_prime, reverse=True)