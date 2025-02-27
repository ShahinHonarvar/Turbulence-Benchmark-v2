def all_left_truncatable_prime(seq):
    answer = [i for j, i in enumerate(seq) if j > 174 and is_prime(i) and is_truncatable(i)]
    answer.sort()
    return answer

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_truncatable(number):
    str_number = str(number)
    if '0' in str_number:
        return False
    for i in range(1, len(str_number)):
        if not is_prime(int(str_number[i:])):
            return False
    return True