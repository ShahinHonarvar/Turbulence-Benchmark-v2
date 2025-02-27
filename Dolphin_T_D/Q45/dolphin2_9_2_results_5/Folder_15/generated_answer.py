import string

def palindromes_between_indices(s):
    p = set()
    for i in range(2, len(s) + 1):
        letters = set(s[1:i])
        for letter in string.ascii_lowercase + string.ascii_uppercase:
            if letter in letters:
                p.add(letter)
                p.add(letter.lower())
    ret = set()
    for i in p:
        for j in p:
            if i != j:
                for k in p:
                    if k != j and i + j + k in p and (i == k):
                        ret.add(i + j + k)
    return ret