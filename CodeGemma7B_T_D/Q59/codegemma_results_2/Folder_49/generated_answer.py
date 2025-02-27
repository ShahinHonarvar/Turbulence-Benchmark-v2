def all_left_truncatable_prime(tupple):
    candidate = tupple[14]
    divisor = 2
    left_truncatable_prime = list()
    while divisor <= candidate:
        if candidate % divisor == 0:
            is_prime = True
            temp = candidate
            while temp // divisor != 0:
                temp = temp // divisor
                if temp % divisor != 0:
                    is_prime = False
                    break
            if is_prime:
                left_truncatable_prime.append(candidate)
        divisor += 1
    return left_truncatable_prime