from itertools import count

def right_truncatable(prime):
    plist = str(prime)
    for i in reversed(range(len(plist))):
        if plist[i] != '0' and int(plist[i:]) in primelist and (int(plist[i:]) not in right_truncatable_prime):
            right_truncatable_prime.append(int(plist[i:]))

def all_right_truncatable_prime(p):
    if p[803] >= min(right_truncatable_prime):
        return sorted(list(filter(lambda x: x < p[803], right_truncatable_prime)))
    return []