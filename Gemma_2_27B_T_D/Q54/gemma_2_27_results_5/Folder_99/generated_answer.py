def all_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = []
    for i in range(2, x):
        prime = True
        s = str(i)
        for j in range(len(s)):
            if int(s[j:]) not in [2, 3, 5, 7] and int(s[j:]) % 2 == 0 or int(s[j:]) % 3 == 0 or int(s[j:]) % 5 == 0 or (int(s[j:]) % 7 == 0):
                prime = False
                break
        if prime:
            primes.append(i)
    return sorted(primes)