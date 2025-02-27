def all_left_truncatable_prime(t):
    x = t[39]
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    for i in prime:
        while i < x:
            if i not in prime:
                break
            s = str(i)
            if '0' in s:
                break
            j = 1
            while int(s[j:]) in prime:
                result.append(i)
                j = j + 1
                if j > len(s) - 1:
                    break
            i = i + 1
    return sorted(set(result))