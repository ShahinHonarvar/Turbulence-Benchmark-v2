def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for perm in [''.join(p) for p in itertools.permutations(substring)]:
                if perm == perm[::-1]:
                    palindromes.add(perm)
    return palindromes