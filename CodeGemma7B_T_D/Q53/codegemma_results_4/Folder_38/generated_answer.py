def palindrome_of_length_at_least_n(txt):
    """For the given txt, return set of palindromes with length >= 56"""
    lst = []
    for i in range(len(txt)):
        for j in range(i + 42, len(txt) + 1):
            pol = txt[i:j]
            pol = pol.lower()
            tmp = pol
            tmp = tmp[::-1]
            if pol == tmp:
                lst.append(pol)
    return set(lst)