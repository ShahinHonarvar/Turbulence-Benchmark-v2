def palindromes_of_specific_lengths(s):
    result_set = set()
    if len(s) < 300:
        return result_set
    s = s[1:300]
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    for length in range(3, 11):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result_set.add(substring)
    return result_set