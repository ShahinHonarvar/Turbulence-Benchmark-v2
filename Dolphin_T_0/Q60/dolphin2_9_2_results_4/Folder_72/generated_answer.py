def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for n in range(x, 1, -1):
        if n in (0, 1):
            continue
        m_n = n
        while m_n:
            if m_n < 10 and is_prime(m_n):
                primes.append(m_n)
            elif not is_prime(m_n):
                break
            m_n //= 10
        m_n = n
        while m_n:
            if m_n < 10 and is_prime(m_n):
                primes.append(m_n)
            elif not is_prime(m_n):
                break
            m_n //= 10
    return primes[::-1]