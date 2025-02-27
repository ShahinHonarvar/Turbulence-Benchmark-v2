def get_palindromes(s):
    return set([s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)) if len(s[i:j + 1]) in range(55, 72) if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and all((c.isalpha() for c in s[i:j + 1]))])

def palindromes_of_specific_lengths(s):
    return get_palindromes(s[13:91])