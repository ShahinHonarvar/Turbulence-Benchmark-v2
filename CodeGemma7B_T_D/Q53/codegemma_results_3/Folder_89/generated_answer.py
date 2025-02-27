def palindrome_of_length_at_least_n(s):
    return {''.join(p) for p in product(*(c * i for c in s.lower() for i in range(1, 51))) if p == p[::-1]}