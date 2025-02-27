from sympy import isprime

def all_left_truncatable_prime(arr):
    x = arr[81]
    result = []
    for i in range(x):
        if isprime(i):
            if '0' not in str(i):
                copy = i
                position = len(str(i))
                while copy > 0:
                    copy = int(str(copy)[:-1])
                    if not isprime(copy):
                        break
                    if copy == 0:
                        result.append(i)
    result.sort(reverse=True)
    return result