def all_right_truncatable_prime(a_tuple_of_positive_integers):
    x = a_tuple_of_positive_integers[429]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def trunc_right(n):
        while n > 0:
            if is_prime(n):
                n //= 10
            else:
                return False
        return True

    def right_truncatable_primes(n):
        if is_prime(n) & trunc_right(n):
            return True
        return False

    def loops(n, i=[]):
        if n < 10:
            return i
        i.append(n)
        n //= 10
        return loops(n, i if right_truncatable_primes(n) else i)
    return descending_sort(list(filter(is_prime, [n for n in loops(x)])))

def descending_sort(a_list):
    return sorted(a_list, reverse=True)