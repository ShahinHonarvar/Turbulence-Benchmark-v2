from re import findall

def palindromes_of_specific_lengths(s):
    s = s[13:96]
    letters_only = ''.join(findall('[a-zA-Z]', s)).lower()
    result = set()
    n = len(letters_only)
    for length in range(57, 61):
        for start in range(n - length + 1):
            sub = letters_only[start:start + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result