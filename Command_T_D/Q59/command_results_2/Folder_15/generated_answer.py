import re

def all_left_truncatable_prime(test_list):
    l = re.findall('(?=\\d)([1-9][\\d]*)(\\d)', str(test_list[6]))
    result = []
    for e in l:
        if all((str(p).isprime() for p in range(int(e), test_list[6], -1))):
            result.append(int(e))
    return sorted(result, reverse=True)