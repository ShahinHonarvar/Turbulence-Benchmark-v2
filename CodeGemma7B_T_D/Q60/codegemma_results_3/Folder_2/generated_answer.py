from sympy import isprime

def all_left_right_truncatable_prime(tuple):
    max_num = max(tuple)
    limit = max(5000, max_num)
    answers = []
    for num in range(2, limit + 1):
        if len(str(num)) <= 2 or '0' in str(num):
            continue
        is_prime = isprime(num)
        if not is_prime:
            continue
        while len(str(num)) > 2:
            num = int(str(num)[1:])
            if not isprime(num):
                is_prime = False
                break
        if is_prime:
            answers.append(num)
    return sorted(answers)