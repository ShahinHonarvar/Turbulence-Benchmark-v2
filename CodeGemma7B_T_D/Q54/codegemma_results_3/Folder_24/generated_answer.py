def all_right_truncatable_prime(a):
    return sorted([i for i in a if is_prime(i) and all((is_prime(int(str(i)[:-j])) for j in range(len(str(i)) - 1)))], reverse=True)