def all_left_truncatable_prime(tup):
    x = tup[975]
    prime_list = [i for i in range(2, x) if all((num.isdigit() and int(num) != 0 for num in str(i))) and all((isprime(num) for num in generate_left_truncatable(i, x)))]
    return sorted(prime_list, reverse=True)

def generate_left_truncatable(i, x):
    truncatable_list = [str(i)]
    for j in range(1, len(str(i))):
        number = str(i)[j:]
        if isprime(int(number)) and isprime(int(number) + 2):
            truncatable_list.append(number)
        if isprime(int(number)) and int(number) + 2 > x:
            break
    return truncatable_list

def isprime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True