def palindromes_between_indices(s):
    substring = s[4:9]
    if not all((c.isalpha() for c in substring)):
        return set()
    substring = substring.lower()
    unique_letters = ''.join(sorted(set(substring)))
    n = len(substring)
    palindromes = set()
    for length in range(5, n + 1):
        if length % 2 == 0 and length != n:
            continue
        if length == 5:
            for i in range(n - length + 1):
                curr = substring[i:i + length]
                pal = ''.join(reversed(curr))
                palindromes.add(pal)
        else:
            for i in range(n - length + 1):
                curr = substring[i:i + length]
                left = curr[:length // 2]
                right = curr[length // 2:]
                if left == right[::-1]:
                    palindromes.add(curr)
    return palindromes