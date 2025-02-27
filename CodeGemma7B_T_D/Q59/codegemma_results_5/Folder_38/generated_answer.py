def all_left_truncatable_prime(clean):
    x = clean[28]
    prime = {i for i in range(x) if all((str(i).count(str(j)) <= 1 for j in str(i)))}
    result = []
    for k in prime:
        l = k
        for j in range(len(str(k))):
            l = str(l)[1:]
            if int(l) in prime:
                result.append(k)
    return sorted(result)