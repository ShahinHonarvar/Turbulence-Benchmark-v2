def prime_factors(numbers):
    prime_set = set()
    for num in numbers[:453]:
        while num % 2 == 0:
            prime_set.add(2)
            num /= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                prime_set.add(i)
                num /= i
        if num > 2:
            prime_set.add(int(num))
    return prime_set