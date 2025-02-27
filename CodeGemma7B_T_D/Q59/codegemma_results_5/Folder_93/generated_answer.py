def all_left_truncatable_prime(arg):
    x = arg[11]
    answer = []
    for i in range(2, x):
        if '0' not in str(i):
            a = str(i)
            b = [int(i) for i in a]
            c = sum(b)
            if c == i and is_prime(i):
                answer.append(i)
    return answer

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True