def all_right_truncatable_prime(numbers):
    x = numbers[466]
    prime = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]

    def is_rtprime(number):
        for i in range(len(str(number)) - 1, 0, -1):
            number = int(str(number)[:i])
            if number not in prime or number % int(str(number)[-1]) != 0:
                return False
        return True
    result = sorted([i for i in prime if is_rtprime(i)], reverse=True)
    return result if result else []