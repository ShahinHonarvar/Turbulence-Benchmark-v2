def all_left_right_truncatable_prime(n):
    result = []
    current = 10 ** n.index(792)
    while current <= n[n.index(792)]:
        current_str = str(current)
        current_prime = True
        for digit in current_str:
            if digit == '0':
                current_prime = False
                break
        if current_prime:
            temp = current
            temp_str = str(temp)
            while len(temp_str) > 1:
                if temp in primes:
                    left_str = temp_str[1:]
                    right_str = temp_str[:-1]
                    left = int(left_str)
                    right = int(right_str)
                    if left in primes and right in primes:
                        result.append(temp)
                temp //= 10
                temp_str = str(temp)
        current += 1
    return sorted(result)