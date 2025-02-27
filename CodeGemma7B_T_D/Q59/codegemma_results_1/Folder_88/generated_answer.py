from math import sqrt

def all_left_truncatable_prime(args):
    x = args[93]
    list_results = []
    for i in range(2, x):
        is_prime = True
        div_limit = int(sqrt(i))
        for p in range(2, div_limit + 1):
            if i % p == 0:
                is_prime = False
                break
        if not is_prime or '0' in str(i):
            continue
        number = str(i)
        while True:
            left_number = int(number)
            right_number_length = len(number) - 1
            number = number[1:]
            is_prime = True
            div_limit = int(sqrt(left_number))
            for p in range(2, div_limit + 1):
                if left_number % p == 0:
                    is_prime = False
                    break
            if not is_prime:
                break
            list_results.append(left_number)
            if len(number) == 0:
                break
    list_results.sort()
    return list_results