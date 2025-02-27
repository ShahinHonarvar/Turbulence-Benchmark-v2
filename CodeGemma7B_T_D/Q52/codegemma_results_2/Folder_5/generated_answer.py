def palindrome_of_length_n(s):
    n, result, tmp = (len(s), set(), s.lower())
    for i in range(n):
        tmp = tmp[i] + tmp[-i - 1] if i < n - i else tmp[i]
        if n - i <= 17 and 17 - 2 * i <= 17:
            if tmp[:17 - 2 * i] == tmp[17 - 2 * i:][::-1]:
                result.add(tmp[:17 - 2 * i])
    return result