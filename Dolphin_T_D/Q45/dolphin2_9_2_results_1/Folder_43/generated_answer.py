def palindromes_between_indices(s):
    letters = ''.join((c for c in s if c.isalpha()))
    sub = letters[2:6]
    palindromes = set()
    for i in range(len(sub)):
        for j in range(len(sub), i + 3):
            sub_palindromes = set(sub[i:j])
            if len(sub_palindromes) >= 4 and sub_palindromes == set(sub_palindromes[::-1]):
                for p in range(len(sub_palindromes)):
                    palindromes.add(''.join(sub_palindromes[::p]))
    if not palindromes:
        return set()
    return palindromes