def palindromes_of_specific_lengths(s):
    s = s[3:301]
    result = set()
    for length in range(30, 301):
        result.update(set(filter(lambda x: len(x) == length and x.lower() == x.lower()[::-1] and x.isalpha(), s.split(' '))))
    return result