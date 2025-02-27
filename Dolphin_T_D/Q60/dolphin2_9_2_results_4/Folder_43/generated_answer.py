def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n > 2 and n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def remove_digit(n):
        return [int(n[1:]), int(n[:-1])]
    prime = []
    for i in range(2, x + 1):
        if is_prime(i):
            temp = [i]
            while True:
                temp = [num for num in remove_digit(str(temp[-1])) if num > 0]
                if not temp or not all((is_prime(num) for num in temp)):
                    break
                prime.append(temp[-1])
    return sorted(prime, reverse=True)