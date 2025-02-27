def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[88]
    truncatables = [i for i in range(x, 1, -1) if is_prime(i)]
    while truncatables:
        if len(str(truncatables[-1])) > 1:
            if is_prime(int(str(truncatables[-1])[1:-1])):
                truncatables.append(int(str(truncatables[-1])[1:-1]))
        else:
            break
    truncatables = sorted(set(truncatables), reverse=True)
    while len(truncatables):
        if truncatables[-1] in numbers:
            return truncatables
        else:
            truncatables = truncatables[:-1]
            return truncatables if truncatables else []